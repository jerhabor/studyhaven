/*
    Payment flow is from the stripe documentation: 
    https://stripe.com/docs/js/elements_object/create

    The styling is taken from: 
    https://stripe.com/en-gb/payments/elements
*/

var stripePublishableKey = $('#id_stripe_publishable_key').text().slice(1, -1);
var clientSecretKey = $('#id_client_secret_key').text().slice(1, -1);
var stripe = Stripe(stripePublishableKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontSize: '16px',
        fontFamily: '"Barlow", sans-serif',
        fontSmoothing: 'antialiased',
        '::placeholder': {
            color: '#CFD7DF',
        },
    },
    invalid: {
        color: '#fff',
        ':focus': {
            color: '#dc3545',
        },
    },
};
var card = elements.create('card', {hidePostalCode: true, style: style});
card.mount('#stripe-card');

// Displaying built-in Stripe Messages for when the user
// enters incorrect/invalid card details.
// (https://stripe.com/docs/api/errors)
card.addEventListener('change', function (event) {
    var errorMessageContainer = $('#card-errors');
    if (event.error) {
        var errorMessage = `
            <span class="ml-1" role="alert">
                <i class="fas fa-exclamation"></i>
            </span>
            <span> ${event.error.message}</span>`;
        $(errorMessageContainer).html(errorMessage);
    } else {
        errorMessageContainer.textContent = '';
    }
});

// Handles the submission of the user checkout form
var checkoutForm = $('#checkout-form');

checkoutForm.addEventListener('submit', function(ev) {
    // Prevent the default click event of POST
    ev.preventDefault(); 
    // Instead execute the code below by first disabling
    // the card element and button to prevent any multiple
    // attempts.
    card.update({'disabled': true});
    $('#pay-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecretKey, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        // Checking if there is an error. If so, a message will
        // be rendered as above when the user enter incorrect/
        // invalid card details.
        if (result.error) {
            var errorMessageContainer = $('#card-errors');
            var errorMessage = `
                <span class="ml-1" role="alert">
                    <i class="fas fa-exclamation"></i>
                </span>
                <span> ${result.error.message}</span>`;
            $(errorMessageContainer).html(errorMessage);
            // Re-enable the card element and pay button
            card.update({'disabled': false});
            $('#pay-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                console.log(result.paymentIntent)
                form.submit();
            }
        }
    });
});
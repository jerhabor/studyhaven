/*
    Payment flow is from the stripe documentation: 
    https://stripe.com/docs/js/elements_object/create

    The styling is taken from: 
    https://stripe.com/en-gb/payments/elements
*/

var stripePublishableKey = $('#id_stripe_publishable_key').text().slice(1, -1);
var clientSecretKey = $('#id_client_secret_key').text().slice(1, -1);
var stripe = Stripe(stripePublishableKey);
var elements = stripe.elements({
    fonts: [
        {
            cssSrc: 'https://fonts.googleapis.com/css2?family=Barlow&display=swap'
        }
    ]
});
var style = {
    base: {
        color: '#000',
        fontSize: '16px',
        fontFamily: '"Barlow", sans-serif',
        fontSmoothing: 'antialiased',
        '::placeholder': {
            color: '#aab7c4',
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
var checkoutForm = document.getElementById('checkout-form');

checkoutForm.addEventListener('submit', function(ev) {
    // Prevent the default click event of POST
    ev.preventDefault(); 
    // Instead firstly disable the stripe card element
    // and pay button to prevent any multiple attempts.
    card.update({'disabled': true});
    $('#pay-button').attr('disabled', true);
    // Trigger the payment loading overlay
    $('#checkout-form').fadeToggle(100);
    $('#payment-loading-overlay').fadeToggle(100);
    var saveContact = Boolean($('#id-save-contact').attr('checked'));
    // Due to the use of django's {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecretKey,
        'save_contact': saveContact,
    };
    var url = '/checkout/cached_checkout_info/';

    $.post(url, postData).done(function () {
        // Attempt processing payment by defining the clientSecretKey
        // and payment_method and store billing & shipping details to the
        // payment intent for the webhook handlers.
        stripe.confirmCardPayment(clientSecretKey, {
            payment_method: {
                card: card,
                billing_details: {
                    // Use trim() to remove any excess whitespace
                    name: $.trim(checkoutForm.full_name.value),
                    email: $.trim(checkoutForm.email_address.value),
                    phone: $.trim(checkoutForm.phone_number.value),
                    address:{
                        line1: $.trim(checkoutForm.address_line1.value),
                        line2: $.trim(checkoutForm.address_line2.value),
                        city: $.trim(checkoutForm.city_or_town.value),
                        country: $.trim(checkoutForm.country.value),
                    },
                },
            },
            shipping: {
                name: $.trim(checkoutForm.full_name.value),
                phone: $.trim(checkoutForm.phone_number.value),
                address:{
                    line1: $.trim(checkoutForm.address_line1.value),
                    line2: $.trim(checkoutForm.address_line2.value),
                    city: $.trim(checkoutForm.city_or_town.value),
                    postal_code: $.trim(checkoutForm.postcode.value),
                    country: $.trim(checkoutForm.country.value),
                },
            },
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
                // Fade out the loading overlay
                $('#checkout-form').fadeToggle(100);
                $('#payment-loading-overlay').fadeToggle(100);
                // Re-enable the card element and pay button
                card.update({'disabled': false});
                $('#pay-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    checkoutForm.submit();
                }
            }
        });
    }).fail(function () {
        // If failed, then the error django message will be displayed
        // to the user/customer after page reload from the view, without
        // them being charged.
        location.reload();
    });
});
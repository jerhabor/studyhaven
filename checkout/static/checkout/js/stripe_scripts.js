/*
    Payment flow is from the stripe documentation: 
    https://stripe.com/docs/js/elements_object/create

    The styling is taken from: 
    https://stripe.com/en-gb/payments/elements
*/

var stripe_publishable_key = $('#id_stripe_publishable_key').text().slice(1, -1);
var client_secret_key = $('#id_client_secret_key').text().slice(1, -1);
var stripe = Stripe(stripe_publishable_key);
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
var card = elements.create('card', {style: style});
card.mount('#stripe-card');

// Displaying built-in Stripe Messages (https://stripe.com/docs/api/errors)
card.addEventListener('change', function (event) {
    var errorMessageContainer = $('#card-errors');
    if (event.error) {
        var errorMessage = `
            <span class="ml-1" role="alert">
                <i class="fas fa-exclamation"></i>
            </span>
            <span> ${event.error.message}</span>
        `;
        $(errorMessageContainer).html(errorMessage);
    } else {
        errorMessageContainer.textContent = '';
    }
});
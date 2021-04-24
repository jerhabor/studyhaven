let selectedCountry = $('#id_default_country').val();
if(!selectedCountry) {
    // Apply placeholder colour if not selected
    $('#id_default_country').css('color', '#aab7c4');
};

$('#id_default_country').change(function() {
    // Each time the box changes, store the value of it
    selectedCountry = $(this).val();
    // Apply the designated color to the option
    if(!selectedCountry) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});
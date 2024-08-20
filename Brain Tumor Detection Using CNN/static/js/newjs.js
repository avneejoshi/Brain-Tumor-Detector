$(document).ready(function() {
    $('#imageUpload').on('change', function() {
        var formData = new FormData($('#upload-file')[0]);

        $.ajax({
            url: '/predict',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $('#result span').text(response.result);
                $('.image-section').show();
                $('.loader').hide();
            },
            error: function(jqXHR) {
                $('#result span').text('Error: ' + jqXHR.responseJSON.error);
                $('.image-section').hide();
                $('.loader').hide();
            }
        });
    });

    $('#btn-predict').click(function() {
        $('.loader').show();
    });
});

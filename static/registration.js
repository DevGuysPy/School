$(document).ready(function() {

    $(".choice").change(function () {
        $('.user-form').hide();
        switch ($(this).val()) {
            case "student":
                $('.student-form').show();
                break;
            case 'teacher':
                $('.teacher-form').show();
                break;
            case 'other':
                $('.other-form').show();
                break;
        }
    });

    $('.form-submit').click(function (event) {
        // if <a> or <input>, add
        event.preventDefault();
        $('.error').html('');
        $.ajax({
            method: "POST",
            url: '/registration/',
            data: $('form').serializeArray()
        }).done(function (response) {
            if (response.status == 'ok') {
                document.location.href = "/login/";
            } else {
                debugger;
                for (var key in response.message) {
                    var errorDiv = $(".error." + key);
                    errorDiv.html(response.message[key][0]);

                }
                for (var key in response.message1) {
                    var errorDiv = $(".error." + key);
                    errorDiv.html(response.message1[key][0]);

                }

            }
        }).fail(function (response) {
            alert('Please choose your account type');
        });
    });

    $("form").validate({
           rules: {
               password: {
                   required: true,
                   minlength: 4,
                   maxlength: 20

               } ,

               cfmPassword: {
                   equalTo: "#password",
                   minlength: 4,
                   maxlength: 20
               },
               first_name: {
                   required: true,
                   minlength: 4,
                   maxlength: 20
                },
               last_name: {
                   required: true,
                   minlength: 4,
                   maxlength: 20
                }


           }

    });
});


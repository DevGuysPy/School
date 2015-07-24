$(document).ready(function()
    $('.form-submit').click(function(event){
        event.preventDefault();
        $('.error').html('');
        $.ajax({
            method: "POST",
            url: '/students/',
            data: $('form').serializeArray()
        }).done(function(response){
            if (response.status == 'ok') {
                alert('Success');
            } else {
                for(var key in response.main)
                    var errorDiv = $(".error." + key);
                    errorDiv.html(response.main[key][0])
                    }
                }
            }
        }).fail(function(response){
            alert('Fail :(');
        });
    });
});
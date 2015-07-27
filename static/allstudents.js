$(document).ready(function(){ 
    $('.form-submit').click(function(event){
        event.preventDefault();
        $('.error').html('');
        $(".searchedstudents").html('');
        $.ajax({
            method: "POST",
            url: '/students/',
            data: $('form').serializeArray()
        }).done(function(response){
            if (response.status == 'ok') {
                $('.media').hide();
                for (var student in response.students_with_marks) {
                    var requestResponse = response.students_with_marks[student];
                    var resultDiv = $('#' + requestResponse['id']);
                    resultDiv.show();
                    var markDiv = resultDiv.find('.mark-field');
                    markDiv.html('Average mark: ' + requestResponse['mark']).show();
                }
            } else {
                for(var key in response.main) {
                    var errorDiv = $(".error." + key);
                    errorDiv.html(response.main[key][0])
                    }
                }
        }).fail(function(response){
            alert('Будьте ласкаві, введіть оцінку!');
        });
    });
    $('#show-all-students').click(function() {
        $('.media').show();
    });
});

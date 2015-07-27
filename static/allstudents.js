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
                    var resultDiv = $('#' + response.students_with_marks[student]['id']);
                    resultDiv.show();
                    var markDiv = $('#' + response.students_with_marks[student]['id'] + ' .mark-field');
                    markDiv.html('Average mark: ' + response.students_with_marks[student]['mark']).show();
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

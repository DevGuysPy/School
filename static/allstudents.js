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
    (function () {
    $(document).ready(function () {
        Highcharts.setOptions({
            global: {
                useUTC: false
            }
        });

        $('#container').highcharts({
            chart: {
                type: 'spline',
                animation: Highcharts.svg, // don't animate in old IE
                marginRight: 10,
                events: {
                    load: function () {

                        // set up the updating of the chart each second
                        var series = this.series[0];
                        setInterval(function () {
                            var x = (new Date()).getTime(), // current time
                                y = Math.random();
                            series.addPoint([x, y], true, true);
                        }, 1000);
                    }
                }
            },
            title: {
                text: 'Live random data'
            },
            xAxis: {
                type: 'datetime',
                tickPixelInterval: 150
            },
            yAxis: {
                title: {
                    text: 'Value'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                formatter: function () {
                    return '<b>' + this.series.name + '</b><br/>' +
                        Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                        Highcharts.numberFormat(this.y, 2);
                }
            },
            legend: {
                enabled: false
            },
            exporting: {
                enabled: false
            },
            series: [{
                name: 'Random data',
                data: (function () {
                    // generate an array of random data
                    var data = [],
                        time = (new Date()).getTime(),
                        i;

                    for (i = -19; i <= 0; i += 1) {
                        data.push({
                            x: time + i * 1000,
                            y: Math.random()
                        });
                    }
                    return data;
                }())
            }]
        });
    });
});
});

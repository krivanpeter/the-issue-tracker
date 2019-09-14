var defaultData = []
var labels = []
$.ajax({
    method: 'GET',
    url: 'api/chart/data/',
    data: {},
    success: function(data){
        labels = data.labels;
        defaultData = data.default;
        setChart();
    },
    error: function(error_data){
        console.log("ERROR")
        console.log(error_data)
    }
});

function setChart(){
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Tickets',
                data: defaultData,
                backgroundColor: [
                    'rgba(228, 71, 37, 0.9)',
                    'rgba(0, 0, 0, 0.9)',
                ],
                borderColor: [
                    'rgba(183, 56, 29, 1)',
                    'rgba(0, 0, 0, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })
}

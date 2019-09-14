var defaultData = []
var labels = []
$.ajax({
    method: 'GET',
    url: 'api/chart/data/',
    data: {},
    success: function(data){
        labels_tickets = data.labels_tickets;
        tickets = data.tickets;
        upvotes = data.upvotes;
        setTicketsChart();
        setUpvotesChart();
    },
    error: function(error_data){
        console.log("ERROR")
        console.log(error_data)
    }
});

function setTicketsChart(){
    var ctx = document.getElementById('number_of_tickets').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels_tickets,
            datasets: [{
                data: tickets,
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
            title: {
                display: true,
                text: 'Number of Tickets',
                fontSize: 25
            },
            legend: {
                display: true,
                position: 'right'
            },
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

function setUpvotesChart(){
    var ctx = document.getElementById('number_of_upvotes').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: labels_tickets,
            datasets: [{
                label: labels_tickets,
                data: upvotes,
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
            title: {
                display: true,
                text: 'Number of Upvotes',
                fontSize: 25
            },
            legend: {
                display: false,
                position: 'right'
            },
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


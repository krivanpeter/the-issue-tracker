var defaultData = []
var labels = []
$.ajax({
    method: 'GET',
    url: 'api/chart/data/',
    data: {},
    success: function(data){
        $(".loader").hide()
        labels_tickets = data.labels_tickets;
        labels_packs = data.labels_packs;
        tickets = data.tickets;
        upvotes = data.upvotes;
        bought_packs = data.bought_packs;
        spent_money = data.spent_money;
        setTicketsChart();
        setUpvotesChart();
        setOrdersChart();
        setSpentMoneyChart();
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
                label: "Number of Upvotes",
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

function setOrdersChart(){
    var ctx = document.getElementById('number_of_orders').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels_packs,
            datasets: [{
                label: "Bought Packages",
                data: bought_packs,
                backgroundColor: [
                    'rgba(205, 127, 50, 0.9)',
                    'rgba(211, 211, 211, 0.9)',
                    'rgba(255, 215, 0, 0.9)',
                ],
                borderColor: [
                    'rgba(164, 102, 40, 1)',
                    'rgba(169, 169, 169, 1)',
                    'rgba(218, 165, 32, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Bought Packages',
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

function setSpentMoneyChart(){
    var ctx = document.getElementById('spent_money').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels_packs,
            datasets: [{
                label: "Spent",
                data: spent_money,
                backgroundColor: [
                    'rgba(205, 127, 50, 0.9)',
                    'rgba(211, 211, 211, 0.9)',
                    'rgba(255, 215, 0, 0.9)',
                ],
                borderColor: [
                    'rgba(164, 102, 40, 1)',
                    'rgba(169, 169, 169, 1)',
                    'rgba(218, 165, 32, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Spent Money/Packages',
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
            },
            tooltips: {
                enabled: true,
                mode: 'single',
                callbacks: {
                    label: function(tooltipItems, data) {
                        return tooltipItems.yLabel + ' £';
                    }
                }
            },
        }
    })
}

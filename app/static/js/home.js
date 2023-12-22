document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/house/stats/temp/all.json').then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            return Promise.reject(response);
        }
    }).then(function (data) {
        new Chart(document.getElementById("power-linechart"), {
            type: "line",
            data: {
                datasets: [{
                    data: data.temperatures,
                    fill: false,
                    lineTension: 0,
                    borderColor: 'rgb(75, 192, 192)',
                }]
            },
            options: {
                legend: {
                    display: false,
                },
                scales: {
                    xAxes: [{
                        type: 'time',
                        time: {
                            unit: 'minute',
                            displayFormats: {
                                'minute': 'HH:MM',
                            }
                        },
                        ticks: {
                            autoSkip: true,
                            maxTicksLimit: 10,
                        },
                    }],
                    yAxes: [{
                        display: true,
                        ticks: {
                            autoSkip: true,
                            maxTicksLimit: 15,
                        },
                        scaleLabel: {
                            display: true,
                            labelString: "°C"
                        }
                    }]
                }
            }
        });
    }).catch(function (err) {
        console.warn('Something went wrong.', err);
    });

    fetch('/api/house/power/current.json').then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            return Promise.reject(response);
        }
    }).then(function (data) {
        new Chart(document.getElementById("power-piechart"), {
            type: "pie",
            data: {
                labels: ["Netzbezug (W)", "Solar-Produktion (W)"],
                datasets: [{
                    data: [data.house_consumption, data.solar_production],
                    backgroundColor: [
                        "#cc6600",
                        "#339933"
                    ],
                    borderColor: "transparent"
                }]
            },
            options: {
                maintainAspectRatio: false,
                legend: {
                    display: true
                }
            }
        });
    }).catch(function (err) {
        console.warn('Something went wrong.', err);
    });

    fetch('/api/house/stats/temp/current.json').then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            return Promise.reject(response);
        }
    }).then(function (data) {
        document.getElementById("temperature-outside").textContent = data.temperature_outside;
    }).catch(function (err) {
        console.warn('Something went wrong.', err);
    });

    fetch('/api/zoe/battery/current.json').then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            return Promise.reject(response);
        }
    }).then(function (data) {
        document.getElementById("zoe-battery-state").textContent = data.battery_percent;
        document.getElementById("zoe-mileage").textContent = data.total_mileage;
    }).catch(function (err) {
        console.warn('Something went wrong.', err);
    });
});

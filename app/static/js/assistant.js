var Frontend = (function () {
  var initClock = function () {
    Frontend.updateClock();
    setInterval("Frontend.updateClock()", 60000);
  };

  var initZoeChart = function () {
    var options = {
      series: [67],
      chart: {
        height: 350,
        type: "radialBar",
        offsetY: 0,
      },
      colors: ['#73d8fd'],
      plotOptions: {
        radialBar: {
          startAngle: -180,
          endAngle: 180,
          track: {
            show: false,
          },
          legend: {
            show: false,
          },
        },
      },
      stroke: {
        dashArray: 15
      },
    };

    var chart = new ApexCharts(
      document.querySelector("#zoe-fuel-chart"),
      options
    );
    chart.render();
  };

  return {
    init: function () {
      initClock();
      initZoeChart();
    },

    updateClock: function () {
      $(".clock").html(moment().locale("de").format("LLL"));
    },
  };
})();

$(document).ready(function () {
  Frontend.init();
});

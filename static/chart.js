"use strict";

const options = {
  responsive: true,
};

let ctx = $("#lineChart").get(0).getContext("2d");

$.get("/chart.json", function (data) {
  let myLineChart = new Chart(ctx, {
    type: "line",
    data: data,
    options: options,
  });
  $("#lineLegend").html(myLineChart.generateLegend());
});

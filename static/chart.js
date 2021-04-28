"use strict";

const options = {
  responsive: true,
};

let ctx = $("#lineChart").get(0).getContext("2d");

$.get("/chart.json", (data) => {
  console.log(data);
});

// $.get("/chart.json", function (data) {
//   let myLineChart = new Chart(ctx, {
//     type: "line",
//     data: data,
//     options: options,
//   });
//   $("#lineLegend").html(myLineChart.generateLegend());
// });

// server
// ajax make route /chart.json (line 9 is ajax get request)
// return data from db - sql alchemy
//  callback function (function definition or arrow function) retrives data
// body of callback is what we do with the data
// query that grabs all the information

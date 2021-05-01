"use strict";

// Chart.defaults.scales.linear.min = 0;
// Chart.defaults.scales.linear.max ÷= 10;

const options = {
  responsive: true,
  // scales: {
  //   y: {
  //     suggestedMin: 0,
  //     suggestedMax: 10,
  //   },
  // },
};

let ctx = $("#lineChart").get(0).getContext("2d");

$.get("/chart.json", (data) => {
  const labels = [];
  const hrs_sleep = [];
  const qual_sleep = [];
  const snooze = [];
  const activity_level = [];
  const qual_day = [];

  for (let entry in data) {
    labels.push(entry);
    hrs_sleep.push(data[entry]["hrs_sleep"]);
    qual_sleep.push(data[entry]["qual_sleep"]);
    snooze.push(data[entry]["snooze"]);
    activity_level.push(data[entry]["activity_level"]);
    qual_day.push(data[entry]["qual_day"]);
  }

  let myLineChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        { label: "Hours Slept", data: hrs_sleep },
        { label: "Quality Sleep", data: qual_sleep },
        { label: "Snooze", data: snooze },
        { label: "Activity Level", data: activity_level },
        { label: "Quality of Day", data: qual_day },
      ],
    },
    options: options,
  });
  $("#lineLegend").html(myLineChart.generateLegend());
});

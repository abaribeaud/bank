<template>
    <div>
      <h2>Monthly Expenses</h2>
      <svg ref="lineChart"></svg>
    </div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  import axios from 'axios';
  
  export default {
    data() {
      return {
        chartData: [],
      };
    },
    mounted() {
      this.getData();
    },
    methods: {
      async getData() {
        // Get data from the backend and store it in chartData then draw the chart
        const response = await axios.get('http://127.0.0.1:5000/get_amount_by_month');
        this.chartData = response.data;
        this.drawChart();
      },
      drawChart() {
        // Set the dimensions and margins of the graph
        const margin = { top: 20, right: 20, bottom: 120, left: 120 }; // increase bottom margin to make space for the rotated label
        const width = window.innerWidth * 0.85 - margin.left - margin.right;
        const height = 500 - margin.top - margin.bottom;

        // Set the ranges for the 2 axis
        const x = d3
            .scaleBand()
            .range([0, width])
            .padding(0.1)
            .domain(this.chartData.map((d) => d.year_month));
        
        const y = d3
            .scaleLinear()
            .range([height, 0])
            .domain([d3.min(this.chartData, (d) => d.tr_amount), d3.max(this.chartData, (d) => d.tr_amount)]);

        // Create the svg element
        const svg = d3
            .select(this.$refs.lineChart)
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        // Add the bars
        svg
            .selectAll('rect')
            .data(this.chartData)
            .enter()
            .append('rect')
            .attr('x', (d) => x(d.year_month))
            .attr('y', (d) => y(Math.max(0, d.tr_amount)))
            .attr('width', x.bandwidth())
            .attr('height', (d) => Math.abs(y(d.tr_amount) - y(0)))
            .attr('fill', (d) => d.tr_amount > 0 ? 'green' : 'red');

        // Add the x-axis
        svg
            .append('g')
            .attr('transform', `translate(0,${height})`)
            .call(d3.axisBottom(x))
            .selectAll('text')
            .attr('transform', 'rotate(-45)') // rotate x-axis tick labels by -45 degrees
            .attr('text-anchor', 'end') // align x-axis tick labels to the end of tick
            .attr('font-size', 14);

        // Add the y-axis
        svg
            .append('g')
            .call(d3.axisLeft(y))
            .selectAll('text')
            .attr('font-size', 14);

        // Add the x-axis label
        svg
            .append('text')
            .attr('text-anchor', 'middle')
            .attr('transform', `translate(${width / 2},${height + margin.top + 50})`)
            .attr('font-size', 18)
            .text('Year-Month');
        
        // Add the y-axis label
        svg
            .append('text')
            .attr('text-anchor', 'middle')
            .attr('transform', `translate(-50,${height / 2})rotate(-90)`)
            .attr('font-size', 18)
            .text('Euros (€)');
        },
        
    },
  };
  </script>
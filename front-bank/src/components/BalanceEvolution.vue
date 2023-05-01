<template>
    <div>
      <h2>Balance Evolution</h2>
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
        // Get data from the backend and store it in chartData then draw the chart
        // Use mounted hook to call getData() when the component is mounted
      this.getData();
    },
    methods: {
      async getData() {
        // Get data from the backend and store it in chartData then draw the chart
        const response = await axios.get('http://127.0.0.1:5000/get_balance_evolution');
        this.chartData = response.data;
        this.drawChart();
      },
      drawChart() {
        // Set the dimensions and margins of the graph
        const margin = { top: 20, right: 20, bottom: 120, left: 120 }; // increase bottom margin to make space for the rotated label
        const width = 1400 - margin.left - margin.right;
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

        // Set the line parameters
        const line = d3.line()
            .x((d) => x(d.year_month) + x.bandwidth() / 2)
            .y((d) => y(d.tr_amount));

        // Create the svg element
        const svg = d3
            .select(this.$refs.lineChart)
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        // Add the line
        svg
            .append('path')
            .datum(this.chartData)
            .attr('fill', 'none')
            .attr('stroke', 'steelblue')
            .attr('stroke-width', 2)
            .attr('d', line);
        
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

        // Add x-axis label
        svg
            .append('text')
            .attr('text-anchor', 'middle')
            .attr('transform', `translate(${width / 2},${height + margin.top + 50})`)
            .attr('font-size', 18)
            .text('Year-Month');

        // Add y-axis label
        svg
            .append('text')
            .attr('text-anchor', 'middle')
            .attr('transform', `translate(-60,${height / 2})rotate(-90)`)
            .attr('font-size', 18)
            .text('Euros (€)');

        // Add horizontal line at y=0
        svg
            .append('line')
            .attr('x1', 0)
            .attr('y1', y(0))
            .attr('x2', width)
            .attr('y2', y(0))
            .style('stroke', 'black')
            .style('stroke-width', 1)
            .style('stroke-dasharray', '3,3');

        },
        
    },
  };
  </script>
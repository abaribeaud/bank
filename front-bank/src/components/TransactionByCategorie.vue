<template>
    <div>
      <h2>Transactions par catégories</h2>
      <div ref="chart"></div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import * as d3 from 'd3';
  
  export default {
    props: {
        // The parent component will pass the month and year to this component
      month: {
        type: String,
        required: true
      },
      year: {
        type: String,
        required: true
      }
    },
    watch: {
        // Watch for changes in month and year and call getData() when they change
      month: 'getData',
      year: 'getData'
    },
    methods: {
      async getData() {
        // Get data from the backend and store it in data then draw the chart
        try {
          const response = await axios.get(`http://127.0.0.1:5000/operations_by_category?start_date=${this.year}-${this.month}-01&end_date=${this.year}-${this.month}-${new Date(this.year, this.month, 0).getDate()}`)
          this.data = await response.data;
          this.drawChart()
        } catch (error) {
          console.error(error)
        }
      },
      drawChart() {
        
        // Clear the graph
        d3.select(this.$refs.chart)
            .selectAll('*')
            .remove();

        // Set the dimensions and margins of the graph
        const margin = { top: 50, right: 50, bottom: 100, left: 100 };
        const width = window.innerWidth * 0.85 - margin.left - margin.right;
        const height = 600 - margin.top - margin.bottom;

        const categoryColors = {
          'Courses': 'steelblue',
          'Restaurants': 'orange',
          'Stations essence': 'green',
          'Divertissement': 'red',
          'Shopping': 'purple'
        }

        // Create the svg element
        const svg = d3
            .select(this.$refs.chart)
            .append('svg')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
            .append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        // Declare the bars
        const x = d3
            .scaleBand()
            .range([0, width])
            .padding(0.1)
            .domain(this.data.map((d) => d.cat_label));

        // Declare the x axis
        const y = d3
            .scaleLinear()
            .range([height, 0])
            .domain([d3.min(this.data, (d) => d.tr_amount), d3.max(this.data, (d) => d.tr_amount)]);

        // Add the x axis
        svg
            .append('g')
            .attr('transform', `translate(0,${height})`)
            .call(d3.axisBottom(x))
            .selectAll('text')
            .attr('transform', 'rotate(-45)')
            .attr('text-anchor', 'end')
            .attr('font-size', 14);

        // Add the y axis
        svg
            .append('g')
            .call(d3.axisLeft(y))
            .selectAll('text')
            .attr('font-size', 14);

        // Add the x axis label
        svg
            .append('text')
            .attr('text-anchor', 'middle')
            .attr('transform', `translate(${width / 2},${height + margin.top + 40})`)
            .attr('font-size', 18)
            .text('Catégories');

        // Add the y axis label
        svg
            .append('text')
            .attr('text-anchor', 'middle')
            .attr('transform', `translate(-60,${height / 2})rotate(-90)`)
            .attr('font-size', 18)
            .text('Euros (€)');

        // Add the bars
        svg
            .selectAll('.bar')
            .data(this.data)
            .enter()
            .append('rect')
            .attr('x', (d) => x(d.cat_label))
            .attr('y', (d) => y(Math.max(0, d.tr_amount)))
            .attr('width', x.bandwidth())
            .attr('height', (d) => Math.abs(y(d.tr_amount) - y(0)))
            .attr('fill', (d) => categoryColors[d.cat_label]);
        },
        


    },
    created() {
    // Call getData() when the component is created
      this.getData()
    }
  }
  </script>
  
  <style>
  .bar {
    /* fill: steelblue; */
    fill: steelblue;
  }
  </style>
  
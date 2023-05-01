<template>
    <div>
        <h1>Statistiques</h1>
    </div>
    <div>
        <form>
            <div style="margin-top: 30px;">
                <label for="month-select">Month:</label>
                <select id="month-select" v-model="selectedMonth">
                    <option value="01">January</option>
                    <option value="02">February</option>
                    <option value="03">March</option>
                    <option value="04">April</option>
                    <option value="05">May</option>
                    <option value="06">June</option>
                    <option value="07">July</option>
                    <option value="08">August</option>
                    <option value="09">September</option>
                    <option value="10">October</option>
                    <option value="11">November</option>
                    <option value="12">December</option>
                </select>
            </div>
            <div>
                <label for="year-select">Year:</label>
                <select id="year-select" v-model="selectedYear">
                    <!-- Pass year and month to the backend -->
                    <option v-for="year in availableYears" :key="year" :value="year">{{ year }}</option>
                </select>
            </div>
        </form>
        <div ref="chart"></div>
        </div>
        <div class="stat-container">
            <TransactionByCategorie :month="selectedMonth" :year="selectedYear"></TransactionByCategorie>
        </div>
        <br>
        <div class="stat-container">
            <MonthlySaved></MonthlySaved>
        </div>
        <br>
        <div class="stat-container">
            <BalanceEvolution></BalanceEvolution>
        </div>
</template>
  
<script>
import TransactionByCategorie from '@/components/TransactionByCategorie.vue';
import MonthlySaved from '@/components/MonthlySaved.vue';
import BalanceEvolution from '@/components/BalanceEvolution.vue';

export default {
    name: 'StatistiquesView',
    components: {
        TransactionByCategorie,
        MonthlySaved,
        BalanceEvolution
  },
    data() {
    return {
        selectedMonth: '01',
        selectedYear: '2020',
        availableYears: [2020, 2021, 2022] // replace with the range of available years
    }
  }
}
</script>

<style>
.stat-container {
  background-color: #f5f5f5;
  border-radius: 10px;
  padding: 20px;
  margin-top: 50px;
  max-width: 90%;
  margin: 0 auto;
}
</style>
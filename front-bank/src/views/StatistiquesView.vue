<template>
    <div>
        <h1>Statistiques</h1>
    </div>
    <div>
        <form>
            <div style="margin-top: 30px;">
                <label for="month-select">Mois : </label>
                <select id="month-select" v-model="selectedMonth">
                    <option value="01">Janvier</option>
                    <option value="02">Février</option>
                    <option value="03">Mars</option>
                    <option value="04">Avril</option>
                    <option value="05">Mai</option>
                    <option value="06">Juin</option>
                    <option value="07">Juillet</option>
                    <option value="08">Août</option>
                    <option value="09">Septembre</option>
                    <option value="10">Octobre</option>
                    <option value="11">Novembre</option>
                    <option value="12">Décembre</option>
                </select>
            </div>
            <div>
                <label for="year-select">Année : </label>
                <select id="year-select" v-model="selectedYear">
                    <!-- Pass year and month to the backend -->
                    <option v-for="year in availableYears" :key="year" :value="year">{{ year }}</option>
                </select>
            </div>
        </form>
        <div ref="chart"></div>
        </div>
        <div class="stat-container" style="margin-top: 30px;">
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
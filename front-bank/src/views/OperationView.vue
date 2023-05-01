<template>
    <div>
        <h1>Operations</h1>
        <FormulaireOperation @form-submitted="handleFormSubmitted" />
        <ResumeOperation class="table-operation" :formData="formData" v-if="showFormData" />
        <TableOperation  class="table-operation" ref="formDataSummary" />
    </div>
</template>
  
<script>
import FormulaireOperation from '@/components/FormulaireOperation.vue'
import ResumeOperation from '@/components/ResumeOperation.vue'
import TableOperation from '@/components/TableOperations.vue'


export default {
    name: 'StatistiquesView',
    components: {
        FormulaireOperation,
        ResumeOperation,
        TableOperation
    },
    data() {
        return {
            formData: null,
            showFormData: false
        }
    },
    methods: {
        handleFormSubmitted(formData) {
            this.formData = formData;
            this.showFormData = true;
            console.log(formData)
            this.$refs.formDataSummary.addFormSubmission(formData);
        }
    }
}
</script>

<style>
.table-operation {
  max-width: 90%;
  margin: 0 auto;
}
</style>
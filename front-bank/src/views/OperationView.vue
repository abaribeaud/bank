<template>
    <div>
        <h1>Operations</h1>
        <FormulaireOperation @form-submitted="handleFormSubmitted" />
        <ResumeOperation :formData="formData" v-if="showFormData" />
        <TableOperation ref="formDataSummary" />
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
            this.$refs.formDataSummary.addFormSubmission(formData);
        }
    }
}
</script>
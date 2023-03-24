<template>
    <div>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Montant</th>
                    <th>Destinataire</th>
                    <th>Catégorie</th>
                    <th>Intitulé</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="submission in formSubmissions" :key="submission.id">
                    <td>{{ submission.date }}</td>
                    <td>{{ submission.type }}</td>
                    <td>{{ submission.montant }}</td>
                    <td>{{ submission.destinataire }}</td>
                    <td>{{ submission.categorie }}</td>
                    <td>{{ submission.intitule }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
  

<script>
export default {
    data() {
        return {
            formSubmissions: []
        }
    },
    methods: {
        addFormSubmission(formData) {
            this.formSubmissions.push(formData);
        }
    }
}
</script>
  
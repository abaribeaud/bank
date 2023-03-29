<template>
    <div>
        <h3 class="text-center">Historique des opération</h3>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Montant</th>
                    <th>Destinataire</th>
                    <th>Catégorie</th>
                    <th>Sous catégorie</th>
                    <th>Intitulé</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="submission in formSubmissions" :key="submission.id"
                    :class="submission.type === 'debit' ? 'table-danger' : 'table-success'">
                    <td>{{ submission.date }}</td>
                    <td>{{ submission.type }}</td>
                    <td>{{ submission.montant }}</td>
                    <td>{{ submission.destinataire }}</td>
                    <td>{{ submission.categorie }}</td>
                    <td>{{ submission.sousCategorie }}</td>
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
    mounted() {
        // Récupère les transactions sur l'API Flask
        fetch('http://127.0.0.1:5000/last_10_operations')
            .then(response => {
                return response.json();
            })
            .then(transactions => {
                console.log(transactions)

                transactions.forEach((item) => {
                    this.formSubmissions.push(item);
                });
            })
            .catch(error => {
                console.log(error);
            });
    },
    methods: {
        addFormSubmission(formData) {
            this.formSubmissions.unshift(formData);
        }
    }
}
</script>
  
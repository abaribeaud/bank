<template>
    <div>
        <h3 class="text-center">Historique des opération</h3>
        <!-- Ici on affiche l'historique de nos opération -->
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>Type</th>
                    <th>Date</th>
                    <th>Type</th>
                    <th>Montant</th>
                    <th>Destinataire</th>
                    <th>Catégorie</th>
                    <th>Sous catégorie</th>
                    <th>Intitulé</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>

                <!-- Pour aider à la lecture on utile une opération ternaire -->
                <tr v-for="submission in formSubmissions" :key="submission.id"
                    :class="submission.type === 'debit' ? 'table-danger' : 'table-success'">
                    <td><i :class="submission.type === 'debit' ? 'fa-solid fa-minus' : 'fa-solid fa-plus'"></i></td>
                    <td>{{ submission.date }}</td>
                    <td>{{ submission.type }}</td>
                    <td>{{ submission.montant }}</td>
                    <td>{{ submission.destinataire }}</td>
                    <td>{{ submission.categorie }}</td>
                    <td>{{ submission.sousCategorie }}</td>
                    <td>{{ submission.intitule }}</td>
                    <td><button class="fa-solid fa-trash" @click="deleteFormSubmission(submission.id)"></button></td>
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

                // Ajout de chaque transaction dans notre tableau
                transactions.forEach((item) => {
                    this.formSubmissions.push(item);
                });
            })
            .catch(error => {
                console.log(error);
            });
    },
    methods: {
        // Ajout d'une nouvelle transaction avec le formulaire
        // On ajoute la nouvelle transaction au début du tableau pour la faire
        addFormSubmission(formData) {
            this.formSubmissions.unshift(formData);
        },

        deleteFormSubmission(id) {

            fetch('http://127.0.0.1:5000/delete_operations/' + id, {
                method: 'DELETE',
                body: id
            })
                .then(response => {
                    if (response.ok) {
                        const index = this.formSubmissions.findIndex((submission) => submission.id === id);
                        if (index !== -1) {
                            this.formSubmissions.splice(index, 1);
                        }
                        return response.json();
                    } else {
                        throw new Error('Erreur lors de la suppression des données');
                    }
                })
                .catch(error => {
                    console.log(error);
                });


        }
    }
}
</script>
  
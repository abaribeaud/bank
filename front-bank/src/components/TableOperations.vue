<template>
    <div>
        <h3 class="text-center">Historique des opération</h3>
        <!-- Here we display the history of our operations -->
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

                <!-- To help the reading we use a ternary operation -->
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
        // Retrieves operations from the Flask API
        fetch('http://127.0.0.1:5000/last_10_operations')
            .then(response => {
                return response.json();
            })
            .then(transactions => {
                console.log(transactions)

                // Adding each operations to our table
                transactions.forEach((item) => {
                    this.formSubmissions.push(item);
                });
            })
            .catch(error => {
                console.log(error);
            });
    },
    methods: {
        // Adding a new operation in the form
        // We add the new transaction at the beginning of the table
        addFormSubmission(formData) {
            this.formSubmissions.unshift(formData);
        },

        // Deleting an operation from the history
        deleteFormSubmission(id) {

            // The deletion is triggered by a click on the trash icon
            // To avoid errors we ask for a confirmation 
            const confirmation = prompt("Si vous souhaitez vraiment supprimer cette opération entré \"supprimer\":");
            if (confirmation === "supprimer") {
                // Call to the API to delete the identified operation
                fetch('http://127.0.0.1:5000/delete_operations/' + id, {
                    method: 'DELETE',
                    body: id
                })
                    // If the api answer is successfull, then we delete the line locally too
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
}
</script>
  
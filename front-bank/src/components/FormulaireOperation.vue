<template>
    <div class="container">
        <form>
            <div class="row">
                <div class="col-sm-6 form-group">
                    <i class="fa-solid fa-calendar-days" style="margin-right: 10px;"></i>
                    <label for="date">Date</label>
                    <input type="date" class="form-control" id="date" v-model="date">
                </div>
                <div class="col-sm-6 form-group">
                    <i class="fa-solid fa-pen" style="margin-right: 10px;"></i>
                    <label for="intitule">Intitulé de l'opération</label>
                    <input type="text" class="form-control" id="intitule" v-model="intitule">
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-sm-6 form-group">
                    <i class="fa-solid fa-dollar-sign" style="margin-right: 10px;"></i>
                    <label for="montant">Montant</label>
                    <input type="number" class="form-control" id="montant" v-model="montant">
                </div>
                <div class="col-sm-6 form-group">
                    <i class="fa-solid fa-person" style="margin-right: 10px;"></i>
                    <label for="destinataire">Nom du destinataire</label>
                    <input type="text" class="form-control" id="destinataire" v-model="destinataire">
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-sm-6 form-group">
                    <i class="fa-solid fa-layer-group" style="margin-right: 10px;"></i>
                    <label for="categorie">Catégorie</label>
                    <select class="form-control" id="categorie" v-model="categorie">
                        <option v-for="cat in categories" :key="cat.cat_id" :value="cat">{{ cat.cat_label }}
                        </option>
                    </select>
                </div>
                <div class="col-sm-6 form-group">
                    <i class="fa-solid fa-list" style="margin-right: 10px;"></i>
                    <label for="sousCategorie">Sous-catégorie</label>
                    <select class="form-control" id="sousCategorie" v-model="sousCategorie">
                        <option v-for="sub in subCategories" :key="sub.sub_id" :value="sub.sub_label">{{ sub.sub_label }}
                        </option>
                    </select>
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-sm-6 form-group d-flex align-items-end">
                    <button type="submit" class="btn btn-success" @click.prevent="submitForm"
                        :disabled="!validateForm()">Envoyer</button>
                </div>
            </div>
        </form>
    </div>
</template>
  
<script>

export default {
    name: 'FormulaireOperation',
    data() {
        return {
            categories: [],
            souscat: [],
            date: '',
            type: '',
            montant: '',
            destinataire: '',
            categorie: '',
            intitule: '',
            sousCategorie: ''
        }
    },
    mounted() {
        // Récupère les catégories sur l'API Flask
        fetch('http://127.0.0.1:5000/categories')
            .then(response => {
                return response.json();
            })
            .then(categories => {
                this.categories = categories;
            })
            .catch(error => {
                console.log(error);
            });

        // Récupère les sous-catégories sur l'API Flask
        fetch('http://127.0.0.1:5000/sous_categories')
            .then(response => {
                return response.json();
            })
            .then(subCategories => {
                this.souscat = subCategories;
            })
            .catch(error => {
                console.log(error);
            });
    },
    methods: {
        validateForm() {
            if (this.date && this.montant && this.destinataire && this.categorie && this.intitule && this.sousCategorie) {
                return true;
            } else {
                return false;
            }
        },
        submitForm() {
            console.log(this.categorie)
            this.$emit('form-submitted', {
                date: this.date,
                type:  this.montant < 0 ? 'debit' : 'credit',
                montant: this.montant,
                destinataire: this.destinataire,
                categorie: this.categorie.cat_label,
                sousCategorie: this.sousCategorie,
                intitule: this.intitule
            });

            this.date = '';
            this.type = '';
            this.montant = '',
            this.destinataire = '',
            this.categorie = '',
            this.sousCategorie = '',
            this.intitule = ''
        }
    },
    computed: {
        subCategories() {
            return this.souscat.filter(souscat => {
                return souscat.sub_cat === this.categorie.cat_id
            })
        }
    }
}
</script>
  
<style scoped>
/* Styles du formulaire ici */
</style>
  


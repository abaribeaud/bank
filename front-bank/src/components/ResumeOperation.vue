<template>  
        <br>      
        <div class="alert alert-info" style="max-width: 90%;margin: 0 auto;" role="alert">
            <h3 class="text-center">Résumé de l'opération</h3>
            <div class="container-fluid">
                <div class="row">
                    <div class="col">
                        <p class="mb-0"><strong>Type:<br></strong> {{ formData.type }}</p>
                    </div>
                    <div class="col">
                        <p class="mb-0"><strong>Date:<br></strong> {{ formData.date }}</p>
                    </div>
                    <div class="col">
                        <p class="mb-0"><strong>Montant:<br></strong> {{ formData.montant }}</p>
                    </div>
                    <div class="col">
                        <p class="mb-0"><strong>Destinataire:<br></strong> {{ formData.destinataire }}</p>
                    </div>
                    <div class="col">
                        <p class="mb-0"><strong>Categorie:<br></strong> {{ formData.categorie }}</p>
                    </div>
                    <div class="col">
                        <p class="mb-0"><strong>Sous cat:<br></strong> {{ formData.sousCategorie }}</p>
                    </div>
                    <div class="col">
                        <p class="mb-0"><strong>Intitulé:<br></strong> {{ formData.intitule }}</p>
                    </div>
                </div>
            </div>
        </div>
        <br>
</template>
    
<script>
export default {
    name: 'ResumeOperation',

    // Récéption du formulaire lorqu'il est envoyé
    props: {
        formData: {
            type: Object,
            required: false
        }
    }
}
</script>
  
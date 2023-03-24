<template>        
        <div class="alert alert-success" role="alert">
            <h3 class="text-center">Résumé de l'opération</h3>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-sm-2">
                        <p class="mb-0"><strong>Type:</strong> {{ formData.type }}</p>
                    </div>
                    <div class="col-sm-2">
                        <p class="mb-0"><strong>Date:</strong> {{ formData.date }}</p>
                    </div>
                    <div class="col-sm-2">
                        <p class="mb-0"><strong>Date:</strong> {{ formData.montant }}</p>
                    </div>
                    <div class="col-sm-2">
                        <p class="mb-0"><strong>Date:</strong> {{ formData.destinataire }}</p>
                    </div>
                    <div class="col-sm-2">
                        <p class="mb-0"><strong>Date:</strong> {{ formData.categorie }}</p>
                    </div>
                    <div class="col-sm-2">
                        <p class="mb-0"><strong>Date:</strong> {{ formData.intitule }}</p>
                    </div>
                </div>
            </div>
        </div>
</template>
    
<script>
export default {
    name: 'ResumeOperation',
    props: {
        formData: {
            type: Object,
            required: false
        }
    }
}
</script>
  
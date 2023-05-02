<template>
    <div class="container">
        <div>
            <h1>Bienvenue sur Ma banque</h1>
            <p>Cette application vous permet de gérer votre argent et de suivre vos opérations bancaires.</p>
        </div>
        <button class="btn">
            <router-link to="/statistiques">
                <img class="img-icon" src="@/assets/stats.png" alt="Statistiques">
            </router-link>
            <br>
            Statistiques
        </button>
        <button class="btn">
            <router-link to="/operations">
                <img class="img-icon" src="@/assets/ope.png" alt="Operations">
            </router-link>
            <br>
            Opérations
        </button>
    </div>
</template>
  
<script>
export default {
    name: 'HomeView',
}
</script>



<style>
.btn {
    background-color: #a8e7a8;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin: 10px;
    height: 20;
}

.img-icon {
    height: 20vh;
}

.container {
    height: 74vh;
}

</style>
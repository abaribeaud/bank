<template>
<footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top" style="max-width: 90%;margin: 0 auto;">
    <p class="col-md-4 text-left">© 2023 Bank</p>

    <a href="https://github.com/abaribeaud/bank" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40" height="40"/>
    </a>

    <ul class="nav col-md-4 justify-content-end">
      <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Home</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Pricing</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">FAQs</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">About</a></li>
    </ul>
  </footer>
  </template>
  
  
  <script>
  export default {
    name: 'FooterGlobal'
  }
  </script>
  
  <style scoped>
  footer {
    font-size: 0.9rem;
  }
  
  /* Styles pour la liste d'éléments */
  ul.list-unstyled li {
    display: inline-block;
  }
  
  /* Styles pour les liens */
  ul.list-unstyled li a {
    color: #fff;
    text-decoration: none;
    transition: color 0.2s;
  }
  
  ul.list-unstyled li a:hover {
    color: #f8f9fa;
  }
  </style>
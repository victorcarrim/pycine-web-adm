<script>
  import Home from "./lib/Home.svelte";
import Artist from "./lib/SearchArtist.svelte";
  import SearchArtist from "./lib/SearchArtist.svelte";
  import User from "./lib/User.svelte";

  let atual = 1;
</script>

<nav class="navbar navbar-expand-lg">
  <div class="container-fluid">
    <a class="navbar-brand" href="http://localhost:5173">Pycine</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" on:click={() => atual = 1}>Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" on:click={() => atual = 2}>Buscar Artista</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" on:click={() => atual = 3}>Administrar Usuários</a>
        </li>
    </div>
  </div>
</nav>

<main>
  {#if atual == 1}
    <Home />
  {/if}
  {#if atual == 2}
    <SearchArtist />
  {/if}
  {#if atual == 3}
    <User />
  {/if}
</main>

<style>
   .navbar {
    background-color: white;
  }
</style>

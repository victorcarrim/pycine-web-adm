<script>
  import { each } from "svelte/internal";

    let promisse = getArtist();
    let name_artist = '';
    let error_search;
    
    async function getArtist() {
        error_search = false;
        const response = await fetch('http://localhost:8000/person/'+ name_artist);
        const artist_information = await response.json();
        if(response.ok){
            return artist_information;
        } else if (response.status == 404) {
            error_search = true;
            return artist_information;
        }
    }

    function handleClick() {
       promisse = getArtist();
    }

</script>

<!-- svelte-ignore a11y-label-has-associated-control -->
<div class="card">
    <div class="card-body">
        <label class="card-title">Digite o nome do Artista: </label>
        <input class="card-text" bind:value={name_artist}>
        <button on:click={handleClick}>Buscar</button>
        </div>
</div>
{#await promisse}
<div class="spinner-border" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
{:then artist}
{#if error_search === true}
    <div class="card card-artist">
        <div class="card-body">
            <h3>Artista não encontrado</h3>
        </div>
    </div>
{/if}
{#if error_search === false}
<div class="card card-artist">
    <img src="{artist.profile_path}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{artist.name}</h5>
      <p class="card-text">{artist.biography}</p>
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item">Nascimento: {artist.birthday}</li>
      <li class="list-group-item">Cidade Natal: {artist.place_of_birth}</li>
      <li class="list-group-item">Profissao Principal: {artist.known_for_department}</li>
      {#if artist.deathday}
        <li class="list-group-item">Falecimento: {artist.deathday}</li>
      {/if}
    </ul>
    {#if artist.homepage != null}
        <div class="card-body">
            <a href="{artist.homepage}" class="card-link">Site</a>
        </div>
    {/if}
</div>
{/if}
{:catch error}
{#if error_search === true}
    <div class="card card-artist">
        <div class="card-body">
            <h3>Artista não encontrado</h3>
        </div>
    </div>
{/if}

{/await}

<style>
    .card{
        align-items: center;
        margin: 5%;
        background-color: white;
    }

    .card-body{
        width: 50%;
        background-color: white;
    }

    .card-img-top{
        width: 15%;
    }

    .card-artist{
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 3%;
    }

    h3{
        align-items: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }



</style>
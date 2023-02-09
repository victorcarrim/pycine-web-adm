<script>
  import { identity } from "svelte/internal";


    let promisse = getMovies();
    let usuários = getUsers();

    let user_id;
    let movie_id;
    let cadastro = false;

    async function getMovies(){
            const response = await fetch('http://18.229.132.40/movies');
            const users = await response.json();
            if(response.ok){
                return users;
            } else {
                throw new Error(users);
            }
        }

    async function getUsers(){
        const response = await fetch('http://18.229.132.40/user/getall');
        const users = await response.json();
        if(response.ok){
            return users;
        } else {
            throw new Error(users);
        }
    }

    async function createMovieFavorite() {
    const response = await fetch('http://18.229.132.40/users/' + user_id + '/' + movie_id , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    });
    const user = await response.json();
    if(response.ok){
        return user;
        cadastro = true;
    } else {
        throw new Error(user);
    }

}

    function create(movie) {
        // @ts-ignore
        user_id = document.getElementById("selected-id").value;
        movie_id = movie.id;
        createMovieFavorite();
    }



</script>

{#await promisse}
    <div class="spinner-border" role="status">
        <span class="visually-hidden">Carregando Filme...</span>
      </div>
    {:then movies} 
        <div class="list-group">
                {#each movies as movie}
                    <div class="card card-artist">
                        <img src="{movie.profile_path}" class="card-img-top" alt="Não Carregado">
                        <div class="card-body">
                        <h5 class="card-title">{movie.title}</h5>
                        <p class="card-text">{movie.overview}</p>
                        </div>
                        <ul class="list-group list-group-flush">
                        <li class="list-group-item">Data de Lançamento: {movie.release_date}</li>
                        <li class="list-group-item">Popularidade: {movie.popularity}</li>
                        <li class="list-group-item">Nota: {movie.vote_avarage}</li>
                        </ul>
                    </div>
                    <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                        Adicionar como favorito
                    </button>
                    <div class="collapse" id="collapseExample">
                        <div class="card card-body">
                            {#await usuários}
                                <div class="spinner-border" role="status">
                                    <span class="visually-hidden">Carregando Usuários...</span>
                                </div>
                                {:then user} 
                                    <div class="list-group">
                                        <select class="form-select" aria-label="Default select example" id="selected-id">
                                            <option value=0 selected>Selecione o usuário</option>
                                            {#each user as user}
                                                <option value="{user.id}">{user.name}</option>
                                            {/each}
                                        </select>
                                    </div>
                                    <button type="submit" class="btn btn-primary" on:click={() => create(movie)}>Cadastrar</button>
                            {/await} 
                        </div>
                    </div>
                {/each}
            </div>
    {/await}


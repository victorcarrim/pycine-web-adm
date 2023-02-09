<script>
  import { each } from "svelte/internal";
  import { get } from "svelte/store";

    let promisse = getUsers();
    let getMovies = false
    let moviesPromisse = getMoviesUser();

    let id;
    let name;
    let email;
    let password;

    async function getUsers(){
        const response = await fetch('http://localhost:8000/user/getall');
        const users = await response.json();
        if(response.ok){
            return users;
        } else {
            throw new Error(users);
        }
    }

    async function getMoviesUser(){
        const response = await fetch('http://localhost:8000/movies/' + id);
        const movies = await response.json();
        if(response.ok){
            let moviesList = [];
            movies.forEach(movieObject => {
                let movie = getMovieByID(movieObject.movie_id);
                let moviepromisse = Promise.resolve(movie);
                moviepromisse.then(function(value) {
                    moviesList.push(value);
                });
            });
            return moviesList;
        } else {
            throw new Error(movies);
        }
    }

    async function getMovieByID(movie_id){
        const response = await fetch('http://localhost:8000/movies/get-movie-by-id/' + movie_id);
        const movie = await response.json();
        if(response.ok){
            return movie;
        } else {
            throw new Error(movie);
        }
    }
    
    async function postUser() {

        const response = await fetch('http://localhost:8000/user/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })
        });
        const user = await response.json();
        if(response.ok){
            return user;
        } else {
            throw new Error(user);
        }
        
    }

    async function deleteUser(){
        const response = await fetch('http://localhost:8000/user/'+ id, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
        });
        const user = await response.json();
        if(response.ok){
            return(user);
        } else {
            throw new Error(user);
        }
    }

    async function updateUser() {
        const response = await fetch('http://localhost:8000/user/' + id, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })
        });
        const user = await response.json();
        if(response.ok){
            return user;
        } else {
            throw new Error(user);
        }
    }

    function userClick(user){
        id = user.id;
        name = user.name;
        email = user.email;
        password = user.password;
        getMovies = true;
        moviesPromisse = getMoviesUser();
    }

    function erease(){
        id = null;
        name = null;
        email = null;
        password = null;
        getMovies = false;
    }

    function create() {
        postUser();
        erease();
        promisse = getUsers();
    }

    function deletee(){
        deleteUser();
        erease();
        promisse = getUsers();
    }

    function update(){
        updateUser();
        erease();
        promisse = getUsers();
    }
</script>

    {#await promisse}
    <div class="spinner-border" role="status">
        <span class="visually-hidden">Carregando Usuários...</span>
      </div>
    {:then user} 
        <div class="list-group">
                {#each user as user}
                    <button on:click={() => userClick(user)} value="{user.id}">{user.name}</button>
                {/each}
        </div>
    {/await}


    <div class="mb-3">
        <label for="name" class="form-label">Nome</label>
        <input type="text" class="form-control" id="name" name="name" bind:value={name}>
    </div>
    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" name="email" bind:value={email}>
    </div>
    <div class="mb-3">
        <label for="password" class="form-label">Senha</label>
        <input type="password" class="form-control" id="password" name="password" bind:value={password}>
    </div>

    {#if id}
        <button type="submit" class="btn btn-primary" on:click={update}>Atualizar</button>
        <button type="submit" class="btn btn-primary" on:click={deletee}>Excluir</button>
    {/if}
    {#if !id}
        <button type="submit" class="btn btn-primary" on:click={create}>Cadastrar</button>
    {/if}
    <button class="btn btn-primary" on:click={erease}>Limpar Campos</button>

    {#if getMovies}
        {#await moviesPromisse}
            <div class="spinner-border" role="status">
                <span class="visually-hidden">Carregando Filmes...</span>
            </div>
        {:then moviesList}
            <div class="list-group">
                {#each moviesList as movie}
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
                {/each}
            </div>
        {/await}
    {/if}
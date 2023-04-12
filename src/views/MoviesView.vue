<template>
    
    <div class="page-header">
        <h2>Movies</h2>
    </div>
    

    <div class="movie-container">
        
        <div class="card movie-card" v-for="movie in movies">

            <div class="movie-image">
                <img class="movie-img" v-bind:src="movie.poster" alt="movie poster"/>
            </div>

            <div class="movie-body">
                <h3 class="card-title">{{ movie.title }}</h3>
                <p class="card-text">{{ movie.description }}</p>
            </div>          
        </div>
    </div>
    
    
</template>
<style>
.page-header {
        text-align: center;
        margin-bottom: 20px;
    }
    .movie-container {
        display: flex;
        flex-wrap: wrap;
        justify-content:flex-start;
        column-gap: 30px;
        padding: 15px;
    }
    .movie-card {
        display: flex;
        flex-direction: row;
        column-gap: 10px;
        width: 400px;
        margin-bottom: 20px;
        box-sizing: border-box;
        height: 500px;
        
    }
    .movie-body{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: 70%;
        object-fit: cover;
    }
    .movie-image {
        display: flex;
        align-items: flex-start;
        width: 30%;
        object-fit: cover;
    }
    .movie-img {
        width: 100%;
        height: 100%;
    }
    
</style>

<script setup>
    import {ref, onMounted} from 'vue'
    let movies = ref([])

    async function fetchMovies(){
        await fetch('/api/v1/movies')
            .then(async response => {
                return await response.json()
            })

            .then(async data => {
                movies.value = await data.movies
            })

            .catch(async errors => {
                console.log(await errors)
            })
    }

    onMounted(() => {
        fetchMovies()
    })
</script>
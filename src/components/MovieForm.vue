<template>
    <div v-if="errors.length > 0" class="alert alert-danger" role="alert">
      <ul>
        <li v-for="error in errors" :key="error">{{ error }}</li>
      </ul>
    </div>
    <div v-if="success" class="alert alert-success" role="alert">
      {{ message }}
    </div>
    <form @submit.prevent="saveMovie" id="movieForm">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" v-model="title" class="form-control" />
      </div>
  
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <input type="text" name="description" v-model="description" class="form-control" />
      </div>
  
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input type="file" name="poster" v-on:change="poster" class="form-control" />
      </div>
  
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </template>
  
  <!-- <script src="https://unpkg.com/vue@3/dist/vue.global.js"> -->
  <script setup>

    import { ref, onMounted } from 'vue'
  
    // const title = ref('')
    // const description = ref('')
    // const poster = ref(0)
    let csrf_token = ref("")
    let errors = ref([])
    let message = ref("Your movie was successfully added!")
    let success = ref(false)
  
    async function getCsrfToken() {
        await fetch('/api/v1/csrf-token')
        .then(async (response) => await response.json())
        .then(async (data) => {
        csrf_token.value = data.csrf_token;
        })
        .catch(async error => console.log(await error))
    }
   

    async function saveMovie() {
        let movieForm = document.getElementById('movieForm')
        let formData = new FormData(movieForm)
      const response = await fetch('/api/v1/movies', {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrf_token.value,
        },
        body: formData
      })

        .then(async response => {
            let result = await response.json()
            return result

        })

        .then(async data => {
            console.log(await data.errors)
            if(typeof await data.errors === undefined){
              errors.value = []
              success.value = true
            }else{
              errors.value = await data.errors
              success.value = false
            }
        })

        .catch(async error => {
            console.log(await error)
        })
    }

    onMounted(() => {
        getCsrfToken()
    })
  </script>
  
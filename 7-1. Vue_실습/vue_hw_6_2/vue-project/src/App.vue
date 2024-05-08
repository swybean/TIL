<template>
  <div>
    <MainPage />

    <RouterLink :to="{ name: 'some' }">Some</RouterLink> |

    <RouterLink :to="{ name: 'other' }">Other</RouterLink>

    <RouterView />
  </div>


</template>



<script setup>
import { RouterLink } from 'vue-router'

import MainPage from '@/components/MainPage.vue'
import SomeView from '@/views/SomeView.vue'

</script>



<style scoped>


</style>

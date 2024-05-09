<template>
  <div>
    <MainPage />
  </div>
</template>


<script setup>
import MainPage from '@/components/MainPage.vue'
import { useFamilyStore } from '@/stores/family'

const store = useFamilyStore()
console.log(store)

</script>



<style scoped>


</style>

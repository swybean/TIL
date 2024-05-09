<template>
    <div>
        <h1>Pinia 연습하기</h1>
        <ParentPage
          class="parent"
          v-for="family in store.familyInfo"
          :key="family.familyName"
          :family="family"
        />
    </div>
</template>

<script setup>
import ParentPage from './ParentPage.vue'
import { useFamilyStore } from '@/stores/family'

const store = useFamilyStore()

</script>

<style scoped>
.parent {
    border: 1px solid rgb(204, 204, 204);
    margin-bottom: 20px;
    background-color: rgb(243, 243, 243);
}
</style>
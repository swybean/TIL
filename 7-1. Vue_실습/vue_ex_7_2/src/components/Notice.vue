<template>
    <div>
        <h2>남은 제품 개수 : {{ store.productCount }}</h2>
    </div>
</template>



<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()
const productCount = store.productCount



</script>



<style scoped>



</style>
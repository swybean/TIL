<template>
    <div>
        <h1>Product List</h1>
        <ul>
            <li v-for="product in store.products">
            {{ product.id }} - {{ product.title }} - {{ product.body }}
            </li>
        </ul>
    </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()



</script>

<style scoped>

</style>
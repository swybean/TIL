<template>
  <div>
    <h1>Product List</h1>
    <ul>
        <li v-for="product in store.products"
          :key="product.id">
          <ProductListItem :product="product" />
        </li>
    </ul>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'
import ProductListItem from './ProductListItem.vue'


const store = useProductStore()
</script>

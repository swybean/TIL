   
<template>
    <div>
      <span>{{ product.id }} - {{ product.title }} - {{ product.body }}</span>
      <button @click="store.deleteProduct(product.id)">Delete</button>
    </div>
</template>




<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()

defineProps({
    product: Object
})


</script>




<style scoped>

</style>
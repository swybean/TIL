import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('products', () => {

    let id = 0
    const products = ref([
        { id: id++, title: 'Product 1', body: 'aaaaaa' },
        { id: id++, title: 'Product 2', body: 'bbbbbb' },
        { id: id++, title: 'Product 3', body: 'cccccc' }
    ])
    return { products }
})

<template>
    <div>
        <h1>부모 페이지입니다.</h1>
        <ChildPage 
          v-for="children in childrens"
          :key="children.id"
          :my-prop="children"
        />
    </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from '@/components/ChildPage.vue'

const childrens = ref([
    { name: '김하나', age: 30 },
    { name: '김두이', age: 20 },
    { name: '김서이', age: 10 },
])

defineProps({
    children: Object,
})

</script>

<style scoped>
div {
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 10px;
}
h3 {
  font-size: 18px;
}
p {
  font-size: 14px;
}
</style>
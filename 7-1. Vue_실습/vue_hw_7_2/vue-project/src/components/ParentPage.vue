<template>
    <div>
        <div class="pbox">
            <h2>부모 컴포넌트</h2>
            <p>{{ family.father }}</p>
            <p>{{ family.mother }}</p>
        </div>
        <ChildPage 
          v-for=" child in family.children"
          :key="child.name"
          :child="child"
        />
    </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue'
import { useFamilyStore } from '@/stores/family'

const store = useFamilyStore()

defineProps({
    family: Object
})

</script>

<style scoped>
.pbox {
    text-align: center;
    
}
</style>
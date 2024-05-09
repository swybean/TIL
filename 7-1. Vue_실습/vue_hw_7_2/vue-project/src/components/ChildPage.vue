<template>
    <div class="childbox">
        <h3>자식 페이지</h3>
        <p>{{ child.name }}</p>
    </div>
</template>

<script setup>
defineProps({
    child: Object
})
</script>

<style scoped>
.childbox {
    text-align: center;
    border: 1px solid rgb(221, 221, 221);
    padding: 10px;
    margin-bottom: 10px;
    background-color: white;
    width: 93%;
    margin-left: auto;
    margin-right: auto;
}
</style>
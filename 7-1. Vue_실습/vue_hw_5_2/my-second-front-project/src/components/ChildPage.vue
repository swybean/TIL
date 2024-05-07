<template>
    <div>
        <h3>자식 페이지입니다.</h3>
        <p>{{ `이름: ${myProp.name}` }}</p>
        <p>{{ `나이: ${myProp.age}` }}</p>
    </div>
</template>

<script setup>
defineProps({
    myProp: Object,
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
<template>
    <div>
        <h2>자식 페이지입니다.</h2>
        <p>{{ `이름 : ${myProp.name}` }}</p>
        <p>{{ `나이 : ${myProp.age}` }}</p>
        <p>{{ `용돈 : ${myProp.balance}` }}</p>
        <button @click="giveMeAllowance(myProp.id)">용돈 주세요.</button>
    </div>
</template>
<!-- 
    3번. ParentPage에서 받은 myProp를 이용해서 이름, 나이, 용돈 등을 받는다. 
    4번. @click="giveMeAllowance(myProp.id)"는 버튼을 눌렀을 때 
        콜백함수 giveMeAllowance를 실행하면서 myProp.id를 넘겨준다.
 -->


<script setup>
defineProps({
    myProp: Object,
})
// 2번. ParentPage에서 넘겨준 my-prop를 여기서 myProp로 받는다고 정의하고 받는다.

const emit = defineEmits(['giveMeAllowance'])

// 5번. 콜백함수 giveMeAllowance가 실행되면 인자로 받은 myPropId를 emit과 함께 ParentPage로 보낸다.
//      emit은 신호만 보내는 것이다. 이 신호를 보낼때 myPropId를 같이 보내주는 것
const giveMeAllowance = function (myPropId) {
    console.log(myPropId)
    emit('giveMeAllowance', myPropId)
    
}

</script>



<style scoped>


</style>
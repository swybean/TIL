<template>
    <div>
        <p>{{ myMsg }}</p>
        <p>{{ dynamicProps }}</p>

        <ParentGrandChild 
          :my-msg="myMsg" 
          @update-name="updateName"
        />

        <button @click="$emit('someEvent')">버튼</button>
        <button @click="buttonClick">버튼2</button>
        <button @click="emitArgs">추가 인자 전달</button>
    </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'

// 내려받은 props를 선언
// defineProps({
//     myMsg: String
// })

// 자바스크립트를 사용해서 변수로 선언해서도 사용가능
const props = defineProps({
    myMsg: String,
    dynamicProps: String,
})

console.log(props)
console.log(props.myMsg)

const emit = defineEmits(['myFocus', 'emitArgs', 'updateName'])

const buttonClick = function () {
    emit('myFocus')
}

const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
    emit('updateName')
}



</script>

<style scoped>

</style>
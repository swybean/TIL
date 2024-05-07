<template>
    <div>
        <h1>부모 페이지입니다.</h1>
        <ChildPage 
          v-for="children in childrens"
          :key="children.id"
          :my-prop="children"
          @give-me-allowance="giveMeAllowance"
          
        />
    </div>
    <!-- 
        1번. ParentPage에서 chidrens를 v-for로 반복하면서 반복한 한 요소 children을 my-prop에 할당해준다.
        이것을 ChildPage.vue로 넘겨준다. 

        7번. @give-me-allowance="giveMeAllowance"로 ChildPage에서 보낸 emit을 받으면 콜백함수 giveMeAllowance를 실행
     -->
</template>


<script setup>
import { ref } from 'vue'
import ChildPage from '@/components/ChildPage.vue';

const childrens = ref([
    { id: 1, name: '김하나', age: 30, balance: 100000 },
    { id: 2, name: '김두이', age: 20, balance: 10000 },
    { id: 3, name: '김서이', age: 10, balance: 1000 },
])


// 8번. 콜백함수 giveMeAllowance를 실행할 때 ChildPage가 넘겨준 myPropId를 인자로 받아 쓰고
const giveMeAllowance = function (myPropId) {
    console.log(myPropId)

    // 9번. 배열 childrens.value를 forEach로 순회하면서 콜백함수를 실행한다.
    // (childrens.value는 위에 const childrens의 배열을 의미한다.)
    childrens.value.forEach(function (children) {
        console.log(children)
        // 10번. 하나씩 순회하면서 만약 children의 id 값과 myPropId로 받은 값이 같다면
        if (children.id === myPropId) {
            console.log(children)
            console.log(children.balance)
            // 11번. 해당 children의 balance 값을 증가시킨다.
            children.balance += 1000
            console.log(children.balance)
        }
    })
    console.log('용돈을 늘려줬다!')
}

</script>


<style scoped>

</style>
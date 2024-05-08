<template>
    <div>
        <h1>학생 상세 정보 목록 입니다.</h1>
        <p v-for="student in students" @click="studentDetail(student.name)">{{ `${student.name} 학생 정보 보기` }}</p>
    </div>
</template>

<!--
     @click="studentDetail(student.name)"를 눌렀을 때 함수가 실행되니까
     함수에서 필요한 매개변수를 여기서 전해줘야한다.  
     여기서는 이미 v-for로 순회를 해서 student를 구해놨으니까 student.name를 바로 찾을 수 잇는 아이고,
     이거를 스크립트 영역에 const studentDetail = function (studentName) 여기에 바로 넘겨준다. 
 -->


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const students = ref([
    { name: '김하나' },
    { name: '김두리' },
    { name: '김서이' },
])

const router = useRouter()

const studentDetail = function (studentName) {
    router.push({ name: 'detail', params: { 'name': studentName }})
}
// 학생 이름은 사용자가 눌렀을 때 입력되는거니까 내가 미리 설정못한다.
// 그래서 위에서 사용자가 클릭했을 때 누른 학생이름을 받아서 써야한다.
</script>



<style scoped></style>
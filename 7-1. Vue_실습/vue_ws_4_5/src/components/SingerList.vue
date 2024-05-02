<template>
    <div class="center-content">
        <h1>가수 정보 페이지에 오신 것을 환영합니다</h1>
        <p>여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</p>
        <img src="@/assets/microphone.jpg" alt="microPhone">
        <h1 class="center-h1"> 가수 목록 </h1>
    </div>
    
    <div class="card">
        <SingerDetail v-for="i in 3" />
    </div>

</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue'

</script>

<style scoped>
img {
    width: 200px;
}
.center-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.center-h1 {
    display: flex;
    flex-direction: column;
    align-items: center;
    color: orangered;

}

.card {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
}
</style>
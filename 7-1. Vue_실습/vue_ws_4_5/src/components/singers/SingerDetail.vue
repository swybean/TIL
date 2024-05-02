<template>

    <div class="card">
        <div class="center-content">
            <h1>가수 이름</h1>
            <img src="@/assets/singer.jpg" alt="singer">
            <p>가수 소개글</p>
            <SingerAlbum />
        </div>
    </div>

</template>

<script setup>
import SingerAlbum from '@/components/singers/SingerAlbum.vue';
</script>

<style scoped>

img {
    width: 200px;
    border-radius: 50%;
}

.card {
    display: inline-block;
    width: 40%;
    margin: 20px;
    padding: 20px;
    border: 1px solid black;
    justify-content: center;
    flex-wrap: wrap;
}

.center-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
}


</style>
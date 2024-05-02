<template>

    <h1 class="center-h1"> 가수 목록 </h1>

    <div class="card">
        <div class="center-content">
            <h1>가수 이름</h1>
            <img src="@/assets/singer.jpg" alt="singer">
            <p>가수 소개글</p>
        </div>
    </div>

    <div class="card">
        <div class="center-content">
            <h1>가수 이름</h1>
            <img src="@/assets/singer.jpg" alt="singer">
            <p>가수 소개글</p>
        </div>
    </div>


</template>

<script setup>

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
</style>
<template>
    <div class="center-content">
        <h1>HAHAHAHA</h1>
    </div>

    <div class="container">
        <div class="brt">
            <h1>가수 이름</h1>
            <img src="@/assets/singer.jpg" alt="ms">
            <p>가수 소개글</p>
        </div>


    </div>
</template>

<script setup>

</script>

<style scoped>
.center-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.brt {
    width: 25%;
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid black;
    box-sizing: border-box;
}

img {
    width: 200px;
    height: 200px;
    border-radius: 50%;
}

.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
</style>
<template>
    <div class="container">
        <div class="gray-box">
            <h4>앨범 제목</h4>
            <p>노래 목록1</p>
            <p>노래 목록2</p>
            <p>노래 목록3</p>
        </div>

        <div class="gray-box">
            <h4>앨범 제목</h4>
            <p>노래 목록1</p>
            <p>노래 목록2</p>
            <p>노래 목록3</p>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>

.gray-box {
    background-color: whitesmoke;
    border: 1px solid gray;
    border-radius: 10px;
    border-color: gray;
    padding: 1px 15px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    text-align: center;
}

p {
    color: orangered;
}

.container {
    display: flex;
    gap: 25px;
    justify-content: center;
}

</style>

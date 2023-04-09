<template>
    <header class='header'>
        <router-link to="/"><h1 class="heading1 logo">ChildEdu</h1></router-link>
        <img class="burger" src="@/img/burger.svg" alt="" @click="clickOnButton">
    </header>
</template>

<style lang='scss' scoped>
    img{
        cursor: pointer;
        transition: 0.3s;
        box-shadow: var(--shadow);
    }

    img:hover{
        transform: translateY(-2.5px);
    }

    .header{
        width: 100vw;
        height: 122px;
        background-color: rgba(63, 140, 255, 1);
        font-weight: bold;
        padding: 0 20px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.07);
        display: flex;
        align-items: center;
        justify-content: space-between;
        z-index: 20;
        position: fixed;
        box-shadow: var(--shadow);
        border-radius: 0px 0px 15px 15px;
    }

    .logo{
        font-family: 'Righteous';
        font-style: normal;
        font-weight: 400;
        font-size: 25px;
        letter-spacing: 0.06em;
        color: #FFFFFF;
        transition: 0.3s;
    }

    .logo:hover{
        transform: translateY(-2.5px);
    }
</style>

<script setup>
    const emit = defineEmits(['click'])
    const clickOnButton = () => {
        emit('click')
    }
</script>

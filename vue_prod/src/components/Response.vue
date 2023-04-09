<script setup>

    const props = defineProps({
        openSidebar: {
            type: Boolean,
            required: true
        },
        right: {
            type: Boolean,
            default: false
        },
        nextStad: {
            type: String,
            required: true,
            default: '/'
        }
        })
</script>

<template>
    <div :class="['sidebar', {sidebar_isopen: openSidebar}]">
        <div v-if="!right">
            <h3 >Плохо(</h3>
            <img src="@/img/retry.svg" alt="" @click="openSidebar = false">
        </div>
        <div v-else>
            <h3 >Хорошо)</h3>
            <router-link :to="nextStad"><img src="@/img/Play.svg" alt="" ></router-link>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    .sidebar{
        color: #fff;
        z-index: 9;
        bottom: 0;
        left: 0;
        background: var(--blue);
        position: fixed;
        width: 100%;
        height: 270px;
        transition: .2s;
        box-shadow: var(--shadow);
        transform: translateY(270px);
        border-radius: 0px 0px 15px 15px;
        &_isopen{
            transform: translateY(0px);
            border-radius: 15px 15px 0px 0px;
        }
        &__link{
            color: #000;
            display: block;
            border-radius: 12px;
            border: 2px solid #fff;
            transition: .2s;
            font-weight: bold;
            margin-bottom: 10px;
            &:hover{
                color: var(--primary);
            }
        }
        & > * {
            display: flex;
            align-items: center;
            justify-content: space-around;
        }
    }
    img{
        width: 50px;
    }
    h3{
        font-size: 30px;
    }
</style>
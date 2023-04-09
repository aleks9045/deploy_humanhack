<script setup>
    import {ref} from 'vue';
    const links = ref([
        {name: 'Чтение', href: '/read/theory1'},
        {name: 'Животные', href: '/animals/theory1'},
        {name: 'Математика', href: '/math/theory1'},
        {name: 'Английский', href: '/english/theory1'}
    ])

    const props = defineProps({
        openSidebar: {
        type: Boolean,
        required: true
        }
})

</script>

<template>
    <div :class="['sidebar', {sidebar_isopen: openSidebar}]">
        <router-link class="sidebar__link"
        v-for="link in links" 
        :key="link.name"
        :to="link.href">{{ link.name }}</router-link>
    </div>
</template>

<style lang="scss" scoped>
    .sidebar{
        z-index: 10;
        left: 0;
        top: 122px;
        height: 100%;
        background: #fff;
        position: fixed;
        width: 250px;
        padding: 20px;
        transition: .2s;
        box-shadow: var(--shadow);
        transform: translateX(-250px);
        &_isopen{
            transform: translateX(0px);
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
    }
</style>
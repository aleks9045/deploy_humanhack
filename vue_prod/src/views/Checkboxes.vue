<script setup>
    import {ref} from 'vue'
    import Checkbox from '@/components/Checkbox/Checkbox.vue'

    const checkboxActive = ref(true)
</script>

<template>
    <h1 class="heading-1">Checkbox</h1>
    <div class="line">
        <Checkbox 
        :label="'Just a checkbox'"
        id="active"
        name="active"
        value="I like it"
        v-model:checked="checkboxActive"/>
    </div>
    
</template>
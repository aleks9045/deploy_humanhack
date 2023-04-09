<script setup>
    
    import {ref} from 'vue'
    import Answer from '@/components/Response.vue'
    const isOpenMenu = ref(false);
    const toggleMenu = () => {
        isOpenMenu.value = !isOpenMenu.value;
        
    }
</script>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                title: 'Default',
                descript: 'Default',
                conditions: 'Default',
                answers: ''
            }
        },
        methods:{
            choose(animal){
                this.answers = animal;
            },
            speech(msg){
                const LANG_RU = 'ru-RU';
                const utterance = new SpeechSynthesisUtterance(msg);
                utterance.lang = LANG_RU;
                utterance.rate = 1.5;
                utterance.pitch = 1.2;
                speechSynthesis.speak(utterance);
            }
        },
        async mounted() {
            const response = await axios.get('http://85.192.41.43/API/animals/task/1?format=json')
            const result = await response.data.task[0]
            this.title = result.content
            this.descript =  result.condition.split(' ')
            this.conditions = result.answer
        }
    }
    
</script>

<template >
    <h1 class="heading-1">Животные</h1>
    <h2 class="heading-2"></h2>
    <div class="practice">
        <p>{{ title }}</p>
        <button class="noneBtn"><img src="../img/loud.svg" alt="" class="loud" @click="speech(title)"></button>
        <div class="one_animal" v-for="animal in descript">
                <img  v-bind:src="`../src/img/${animal}.svg`" alt="" :class="['animal', {'selected': answers === animal}]" @click="choose(animal)">
        </div>
        <div class="next" @click="toggleMenu"><img src="@/img/next.svg" alt=""></div>    
    </div>
    <span v-if="answers === conditions"><Answer :openSidebar="isOpenMenu" v-bind:right="true" :nextStad="'/'"/></span>
    <span v-else ><Answer :openSidebar="isOpenMenu" v-bind:right="false"/></span>
</template>

<style lang="scss" scoped>
    .noneBtn{
        background-color: #fafafa;
        border: none;
    }

    .animal{
        transition: .3s;
    }
    .selected{
        filter: drop-shadow(0px 0px 10px rgba(0, 255, 10, 0.77));
    }

    h1{
        text-align: center;
    }
    .practice{
        text-align: center;
    }
    .next{
        margin-top: 30px;
        width: 100%;
        height: 70px;
        background: var(--green);
        box-shadow: 0px 5px 10px rgba(24, 46, 79, 0.11);
        border-radius: 15px;
        border: none;
        transition: 0.3s;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
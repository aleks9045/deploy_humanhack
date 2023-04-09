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
                content: 'Default',
                conditions: 'Default',
                answers: '',
                letter: '',
                rightAnsw: ''
            }
        },
        methods:{
            choose(pic){
                this.answers = pic;
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
            const response = await axios.get('http://85.192.41.43/API/english/task/1?format=json')
            const result = await response.data.task[0]
            this.title = result.title
            this.rightAnsw = result.answer
            this.conditions = result.condition
            console.log(result);
        }
    }
    
</script>

<template >
    <h1 class="heading-1">Английский</h1>
    <div class="practice">
        <h2 class="heading-2">{{ title }}</h2>
        <h3 class="condition">{{ conditions }}</h3>
        <input v-model="answers" type="text">
    </div>
    <div class="next" @click="toggleMenu"><img src="@/img/next.svg" alt=""></div>
    <span v-if="answers.toUpperCase() === rightAnsw.toLocaleUpperCase()"><Answer :openSidebar="isOpenMenu" v-bind:right="true" :nextStad="'/'"/></span>
    <span v-else ><Answer :openSidebar="isOpenMenu" v-bind:right="false"/></span>
</template>

<style lang="scss" scoped>
    h3{
        font-size: 30px;
    }
    input{
        width: 80%;
        text-align: center;
        outline: none;
        border: none;
        border-bottom: 4px solid #503838;
        transition: 0.3s;
        font-size: 40px;
        color: #000000;
        background-color: #fafafa;
    }

    input:active{
        border-bottom: 4px solid rgba(14, 0, 0, 1);
    }

    .noneBtn{
        margin: 0 auto;
    }
    .practice{
        text-align: center;
    }
    .one_pic *{
        transition: .3s;
    }
    .selected{
        filter: drop-shadow(0px 0px 10px rgba(0, 255, 10, 0.77));
    }

    .pack{
        width: 80%;
        display: flex;
        align-items: center;
        justify-content: space-around;
        margin-top: 50px;
    }
    h2{
        text-align: center;
    }
    .noneBtn{
        background-color: #fafafa;
        border: none;
    }

    h1{
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
    .theory{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
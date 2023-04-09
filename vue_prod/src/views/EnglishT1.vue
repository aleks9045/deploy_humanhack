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
            const response = await axios.get('http://85.192.41.43/API/english/theory/1?format=json')
            const result = await response.data.theory[0]
            this.title = result.title
            this.content = result.content.split('|')
            this.conditions = result.condition.split(' ')
            console.log(result);
        }
    }
    
</script>

<template >
    <h1 class="heading-1">Английский</h1>
    <h2 class="heading-2">{{ title }}</h2>
    <div class="theory">
        <div v-for="pic in conditions" class="tem">
            <img v-bind:src="`../src/img/${pic}.svg`" alt="" class="one_picture">
            <p class="parag">{{ content[conditions.indexOf(pic)] }}</p>
            <button class="noneBtn"><img src="../img/loud.svg" alt="" class="loud" @click="speech(content[conditions.indexOf(pic)])"></button>
        </div>
    </div>
    <router-link to="/english/practice1"><img src="@/img/next.svg" alt="" class="next"></router-link>
</template>

<style lang="scss" scoped>
    .noneBtn{
        height: 50px;
    }

    .one_picture{
        height: 70px;
    }
    .parag{
        text-align: center;
        margin-left: 15px;
    }
    .tem{
        width: 80%;
        margin-top: 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .title-div{
        display: flex;
        justify-content: center;
        text-align: center;
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
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
            const response = await axios.get('http://85.192.41.43/API/read/task/1?format=json')
            const result = await response.data.task[0]
            this.title = result.content
            this.rightAnsw =  result.answer
            this.conditions = result.condition.split(' ')
        }
    }
    
</script>

<template >
    <h1 class="heading-1">Чтение</h1>
    <div class="title-div">
        <h2 class="heading-2">{{ title }}</h2>
        <button class="noneBtn"><img src="../img/loud.svg" alt="" class="loud" @click="speech(title)"></button>
    </div>
    <div class="practice">
        <div class="one_pic" v-for="pic in conditions">
                <img  v-bind:src="`../src/img/${pic}.svg`" alt="" :class="['animal', {'selected': answers === pic}]" @click="choose(pic)">
        </div>
        <div class="next" @click="toggleMenu"><img src="@/img/next.svg" alt=""></div>    
    </div>
    <span v-if="answers === rightAnsw"><Answer :openSidebar="isOpenMenu" v-bind:right="true" :nextStad="'/'"/></span>
    <span v-else ><Answer :openSidebar="isOpenMenu" v-bind:right="false"/></span>
</template>

<style lang="scss" scoped>
    .one_pic{
        margin-top: 50px;
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
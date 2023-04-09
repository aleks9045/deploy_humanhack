<script >
    import axios from 'axios'
    export default {
        data() {
            return {
                descript: 'Default',
                conditions: 'Default'
            }
        },
        methods :{
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
            const response = await axios.get('http://85.192.41.43/API/animals/theory/1?format=json')
            const result = await response.data.theory[0]
            this.descript = result.content.split('|')
            this.conditions =  result.condition.split(' ')
        }
    }

</script>

<template >
    <div id="wrapper">
        <h1 class="heading-1">Животные</h1>
        <h2 class="heading-2"></h2>
        <div class="theory">
            <div class="one_animal" v-for="animal in conditions">
                <img  v-bind:src="`../src/img/${animal}.svg`" alt="" class="animal">
                <p class="animal-desc">{{ descript[conditions.indexOf(animal)] }}</p>
                <button class="noneBtn"><img src="../img/loud.svg" alt="" class="loud" @click="speech(descript[conditions.indexOf(animal)])"></button>
            </div>
            <router-link to="/animals/practice1"><img src="@/img/next.svg" alt="" class="next"></router-link>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    .noneBtn{
        background-color: #fafafa;
        border: none;
    }

    .animal{
        margin-bottom: 0px;
    }

    .heading-1{
        text-align: center;
    }
    .one_animal{
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .animal-desc{
        font-size: 20px;
        margin-bottom: 10px;
        margin-top: 0;
    }

    .loud{
        margin-bottom: 60px;
    }

    .one_animal > *{
        text-align: center;
    }

    .example{
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        & p{
            font-size: 60px;
            color: #000000;
        }
    }
    .plus, .equal{
        width: 50px;
    }

    .number-visual{
        width: 90px;
    }

    @media (max-width: 400px){
        .plus, .equal{
            width: 30px;
        }

        .number-visual{
            width: 60px;
        }
        .example p{
        font-size: 40px;
        }
    }
    .next{
        width: 100%;
        height: 70px;
        background: var(--green);
        box-shadow: 0px 5px 10px rgba(24, 46, 79, 0.11);
        border-radius: 15px;
        border: none;
        transition: 0.3s;
    }
    .next:hover{
        background: var(--green-hover);
    }
</style>
<script>
    import axios from 'axios'
    
    export default {
        data() {
            return {
                title: 'Default',
                descript: 'Default',
                conditions: 'Default'
            }
        },
        async mounted() {
            const response = await axios.get('http://85.192.41.43/API/math/theory/1?format=json')
            const result = await response.data.theory[1]
            this.title = result.title
            this.descript = result.content
            this.conditions =  result.condition.split('\n')
            for (let i=0; i<this.conditions.length; i++){
                this.conditions[i] = this.conditions[i].replace('+', 'plus').replace('=', 'equal').replace('-', 'minus').split(' ')
            }
            console.log(result);
        }
    }
</script>


<template >
    <h1 class="heading-1">Математика</h1>
    <h2 class="heading-2">{{ title }}</h2>
    <div class="theory">
        <p class="diskript">{{ descript }}</p>
        <div class="examples">
            <div class="example">
                <img v-bind:src="`../src/img/${this.conditions[0][0]}.svg`" alt="" class="number-visual">
                <img v-bind:src="`../src/img/${this.conditions[0][1]}.svg`" alt="" class="plus">
                <img v-bind:src="`../src/img/${this.conditions[0][2]}.svg`" alt="" class="number-visual">
                <img v-bind:src="`../src/img/${this.conditions[0][3]}.svg`" alt="" class="equal">
                <p class="answer">{{ this.conditions[0][4] }}</p>
            </div>
            <div class="example">
                <img v-bind:src="`../src/img/${this.conditions[1][0]}.svg`" alt="" class="number-visual">
                <img v-bind:src="`../src/img/${this.conditions[1][1]}.svg`" alt="" class="plus">
                <img v-bind:src="`../src/img/${this.conditions[1][2]}.svg`" alt="" class="number-visual">
                <img v-bind:src="`../src/img/${this.conditions[1][3]}.svg`" alt="" class="equal">
                <p class="answer">{{ this.conditions[1][4] }}</p>
            </div>
            <div class="example">
                <img v-bind:src="`../src/img/${this.conditions[2][0]}.svg`" alt="" class="number-visual">
                <img v-bind:src="`../src/img/${this.conditions[2][1]}.svg`" alt="" class="plus">
                <img v-bind:src="`../src/img/${this.conditions[2][2]}.svg`" alt="" class="number-visual">
                <img v-bind:src="`../src/img/${this.conditions[2][3]}.svg`" alt="" class="equal">
                <p class="answer">{{ this.conditions[2][4] }}</p>
            </div>
            <router-link to="/math/practice2"><img src="@/img/next.svg" alt="" class="next"></router-link>
        </div>
    </div>
    
</template>

<style lang="scss" scoped>
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
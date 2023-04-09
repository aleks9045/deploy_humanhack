import { createRouter, createWebHistory } from "vue-router"
import Index from  '@/views/Index.vue'
import MathT1 from  '@/views/MathT1.vue'
import MathP1 from '@/views/MathP1.vue'
import MathT2 from  '@/views/MathT2.vue'
import MathP2 from '@/views/MathP2.vue'
import MathT3 from  '@/views/MathT3.vue'
import MathP3 from '@/views/MathP3.vue'
import MathGame from '@/views/MathGame.vue'
import AnimalsT1 from '@/views/AnimalsT1.vue'
import AnimalsP1 from '@/views/AnimalsP1.vue'
import ReadingT1 from '@/views/ReadingT1.vue'
import ReadingP1 from '@/views/ReadingP1.vue'
import EnglishT1 from '@/views/EnglishT1.vue'
import EnglishP1 from '@/views/EnglishP1.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path : '/english/practice1',
            name : 'EnglishP1',
            component : EnglishP1
        },
        {
            path : '/english/theory1',
            name : 'EnglishT1',
            component : EnglishT1
        },
        {
            path : '/read/practice1',
            name : 'ReadingP1',
            component : ReadingP1
        },
        {
            path : '/read/theory1',
            name : 'ReadingT1',
            component : ReadingT1
        },
        {
            path : '/animals/practice1',
            name : 'AnimalsP1',
            component : AnimalsP1
        },
        {
            path : '/animals/theory1',
            name : 'AnimalsT1',
            component : AnimalsT1
        },
        {
            path : '/',
            name : 'Index',
            component : Index
        },
        {
            path : '/math/theory1',
            name : 'MathT1',
            component : MathT1
        },
        {
            path : '/math/practice1',
            name : 'MathP1',
            component : MathP1
        },
        {
            path : '/math/theory2',
            name : 'MathT2',
            component : MathT2
        },
        {
            path : '/math/practice2',
            name : 'MathP2',
            component : MathP2
        },
        {
            path : '/math/theory3',
            name : 'MathT3',
            component : MathT3
        },
        {
            path : '/math/practice3',
            name : 'MathP3',
            component : MathP3
        },
        {
            path : '/math/game',
            name : 'MathGame',
            component : MathGame
        }
    ]
})

export default router
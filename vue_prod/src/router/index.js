import { createRouter, createWebHistory } from "vue_prod-router"
import Index from  '@/views/Index.vue_prod'
import MathT1 from  '@/views/MathT1.vue_prod'
import MathP1 from '@/views/MathP1.vue_prod'
import MathT2 from  '@/views/MathT2.vue_prod'
import MathP2 from '@/views/MathP2.vue_prod'
import MathT3 from  '@/views/MathT3.vue_prod'
import MathP3 from '@/views/MathP3.vue_prod'
import MathGame from '@/views/MathGame.vue_prod'
import AnimalsT1 from '@/views/AnimalsT1.vue_prod'

const router = createRouter({
    history: createWebHistory(),
    routes: [
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
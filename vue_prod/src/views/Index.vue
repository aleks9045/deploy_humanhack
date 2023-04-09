<template>
    <div class="_container">
        <h1 class="heading-1">
            Выбери урок
        </h1>
    </div>
        <div class="all_lessons">
            <router-link to="/math/theory1"><div class="lesson math">
                <img src="@/img/math.svg" alt="" class="lesson_preview">
                <p class="lesson_name">
                    МАТЕМАТИКА
                </p>
            </div></router-link>
            <router-link to="/read/theory1"><div class="lesson read">
                <img src="@/img/read.svg" alt="" class="lesson_preview">
                <p class="lesson_name">
                    ЧТЕНИЕ
                </p>
            </div></router-link>
            <router-link to="/animals/theory1"><div class="lesson animals">
                <img src="@/img/animals.svg" alt="" class="lesson_preview">
                <p class="lesson_name">
                    ЖИВОТНЫЕ
                </p>
            </div></router-link>
            <router-link to="/english/theory1"><div class="lesson eng">
                <img src="@/img/eng.svg" alt="" class="lesson_preview">
                <p class="lesson_name">
                    АНГЛИЙСКИЙ
                </p>
            </div></router-link>
        </div>
</template>

<style scoper lang="scss">
    .all_lessons{
        display: flex;
        flex-direction: column;
    }

    .read{
        background: var(--green);
    }

    .animals{
        background: var(--blue);
    }

    .lesson_name{
        font-size: 20px;
        line-height: 22px;
        display: flex;
        align-items: center;
        text-align: center;
        letter-spacing: -0.04em;
        color: #FFFFFF;
    }
    .math, .eng{
        background: var(--pink);
    }
    .lesson{
        margin: 0 auto;
        width: 80%;
        height: 100px;
        box-shadow: 0px 5px 10px rgba(24, 46, 79, 0.11);
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: space-around;
        margin-bottom: 40px;
    }

    ._container{
        text-align: center;
        margin-bottom: 50px;
    }

    .lesson_preview{
        height: 80px;
    }
</style>
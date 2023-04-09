<script setup>
    const props = defineProps({
        label: {
            type: String,
            default: 'button'
        },
        color: {
            type: String,
            default: 'primary'
        },
        rounded: {
            type: Boolean,
            default: false
        },
        disabled: {
            type: Boolean,
            default: false
        },
        outlined: {
            type: Boolean,
            default: false
        },
        icon:{
            type: String,
            required: false
        },
        size: {
            type: String,
            required: false,
            default: 'normal'
        }
    })

    const emit = defineEmits(['click'])

    const clickOnButton = () => {
        emit('click')
    }
</script>

<template>
    <button :class="['btn', `btn_${color}`, 
    {'btn_rounded': rounded}, 
    {'btn_outlinde': outlined},
    {'btn_icon': icon},
    {'btn_icon': icon},
    {'btn_large': size === 'large'}]"
    :disabled="disabled"
    @click="clickOnButton">

        <span v-if="icon">
            <font-awesome-icon :icon="`fa-regular fa-${icon}`" />
        </span>

        <span v-else>
            {{ label }}
        </span>

    </button>

</template>

<style lang="scss" scoped>
    .btn{
        padding: 0 20px;
        height: 40px;
        color: #fff;
        border-radius: 7px;
        border: none;
        cursor: pointer;
        font-size: 15px;
        transition: .2s;
        &_primary{
            background: var(--primary);
            border: 2px solid var(--primary);
            &:enabled:hover{
                background: var(--primary-hover);
            }
        }
        &_success{
            background: var(--success);
            border: 2px solid var(--success);
            &:enabled:hover{
                background: var(--success-hover);
            }
        }
        &_info{
            background: var(--info);
            border: 2px solid var(--info);
            &:enabled:hover{
                background: var(--info-hover);
            }
        }
        &_warning{
            background: var(--warning);
            border: 2px solid var(--warning);
            &:enabled:hover{
                background: var(--warning-hover);
            }
        }
        &_danger{
            background: var(--danger);
            border: 2px solid var(--danger);
            &:enabled:hover{
                background: var(--danger-hover);
            }
        }
        &_second{
            background: var(--second);
            border: 2px solid var(--second);
            &:enabled:hover{
                background: var(--second-hover);
            }
        }
        &_rounded{
            border-radius: 20px;
        }
        &:disabled{
            opacity: 0.6;
            cursor: default;
            &:hover{
                opacity: 0.6;
            }
        }
        &_outlinde{
            background: transparent;
            color: #000;
            &:hover{
                color: #fff;
            }
        }
        &_icon{
            min-width: 40px;
            min-height: 40px;
            padding: 0;
            border-radius: 50%;
        }
        &_large{
            height: 48px;
        }
    }
</style>
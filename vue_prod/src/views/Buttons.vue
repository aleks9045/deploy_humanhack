<script setup>
    import Button from '@/components/Button.vue'

    const eventForButton = () => {
        alert('Enjoy this button!')
    }

</script>

<template>
    <h1 class="heading-1">Buttons</h1>
    <h2 class="heading-2">Colors</h2>
    <div class="line">
        <Button label="Primary" color="primary"/>
        <Button label="Secondary" color="second"/>
        <Button label="Info" color="info"/>
        <Button label="Success" color="success"/>
        <Button label="Warning" color="warning"/>
        <Button label="Danger" color="danger"/>
    </div>
    <h2 class="heading-2">Rounded</h2>
    <div class="line">
        <Button label="Primary" color="primary" rounded/>
        <Button label="Secondary" color="second" rounded/>
        <Button label="Info" color="info" rounded/>
        <Button label="Success" color="success" rounded/>
        <Button label="Warning" color="warning" rounded/>
        <Button label="Danger" color="danger" rounded/>
    </div>
    <h2 class="heading-2">Disabled</h2>
    <div class="line">
        <Button label="Primary" color="primary" disabled/>
        <Button label="Secondary" color="second" disabled/>
        <Button label="Info" color="info" disabled/>
        <Button label="Success" color="success" disabled/>
        <Button label="Warning" color="warning" disabled/>
        <Button label="Danger" color="danger" disabled/>
    </div>
    <h2 class="heading-2">Outlined</h2>
    <div class="line">
        <Button label="Primary" color="primary" outlined/>
        <Button label="Secondary" color="second" outlined/>
        <Button label="Info" color="info" outlined/>
        <Button label="Success" color="success" outlined/>
        <Button label="Warning" color="warning" outlined/>
        <Button label="Danger" color="danger" outlined/>
    </div>
    <h2 class="heading-2">Icons</h2>
    <div class="line">
        <Button icon="heart" color="primary" outlined/>
        <Button icon="lemon" color="second"/>
        <Button icon="address-book" color="info" outlined/>
        <Button icon="hand" color="success"/>
        <Button icon="credit-card" color="warning" outlined/>
        <Button icon="hourglass" color="danger"/>
    </div>
    <h2 class="heading-2">Large</h2>
    <div class="line">
        <Button label="Normal" color="primary"/>
        <Button label="Large" color="second" size="large"/>
        <Button label="Normal" color="info" outlined/>
        <Button label="Large" color="success" outlined size="large"/>
    </div>
    <h2 class="heading-2">Events</h2>
    <div class="line">
        <Button label="Primary" color="primary" @click="eventForButton"/>
    </div>
</template>

<style lang="scss" scoped>
</style>
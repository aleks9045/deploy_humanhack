<script setup>
import LayoutHeader from '@/components/Header.vue'
import LayoutSideBar from '@/components/Sidebar.vue'

import {ref} from 'vue'

const isOpenMenu = ref(false);
const toggleMenu = () => {
  isOpenMenu.value = !isOpenMenu.value;
}

</script>
<template>
  <div class='container'>
    <LayoutHeader @click="toggleMenu"/>
    <LayoutSideBar :openSidebar="isOpenMenu"/>
    <div :class="['content', {content_full: !isOpenMenu}]">
      <router-view/>
    </div>
  </div>
</template>

<style lang="scss">
@import "./styles/global.scss";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.content{
  top: 122px;
  max-width: 1400px;
  margin-left: 250px;
  padding: 15px;
  transition: .2s;
  position: relative;
  &_full{
    margin-left: 0px;
  }

}

@media(max-width: 1023px) {
  .content{
    margin-left: 0;
  }
}
</style>

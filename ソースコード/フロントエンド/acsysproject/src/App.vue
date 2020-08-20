<template>
  <div>
<!--  headerの設定-->
      <LoginHeader v-if="this.$store.state.accountToken" ></LoginHeader>
      <TopHeader v-else-if="!this.$store.state.accountToken"></TopHeader>
      <transition mode="out-in">
          <router-view />
      </transition>
  </div>
</template>

<script>

  import TopHeader from './components/TopHeader.vue'
  import LoginHeader from './components/LoginHeader.vue'

  export default {
    name: 'App',
    components:{
        TopHeader,
        LoginHeader,
    },
  }
</script>

<style>
    /*アニメーションの設定*/
  .v-enter-active, .v-leave-active {
      transition: opacity .3s;
  }
  .v-enter, .v-leave-to {
      opacity: 0;
  }
</style>

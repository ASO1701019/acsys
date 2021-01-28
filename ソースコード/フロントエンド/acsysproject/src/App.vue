<template>
    <div>
<!--  headerの設定-->
      <LoginHeader v-if="this.$store.state.accountToken" ></LoginHeader>
      <TopHeader v-else-if="!this.$store.state.accountToken"></TopHeader>
      <transition mode="out-in">
          <router-view />
      </transition>
      <Loading />
    </div>
</template>

<script>

  import TopHeader from './components/TopHeader.vue'
  import LoginHeader from './components/LoginHeader.vue'
  import Loading from "./components/Loading";

  export default {
    name: 'App',
    components:{
        TopHeader,
        LoginHeader,
        Loading
    },
  }
</script>

<style>
    /*.transition-enter,*/
    /*.transition-leave-to {*/
    /*    opacity: 0;*/
    /*}*/
    /*.transition-enter-active,*/
    /*.transition-leave-active {*/
    /*    transition: opacity 1s;*/
    /*}*/
</style>

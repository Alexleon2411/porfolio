<template>
  <v-app>
    <v-main>
      <NavBar2/>
      <!-- <BackgroundEffect/> -->
     <RouterView/>
    </v-main>

    <AppFooter />
  </v-app>
</template>

<script >
import NavBar2 from './components/NavBar2.vue';
import HelloWorld from './components/HelloWorld.vue'
import HeaDer from './components/HeaDer'
import BackgroundEffect from './components/BackgroundEffect.vue';
import AboutSeccion from './components/AboutSeccion';



export default {
  components:{
    NavBar2,
    HelloWorld,
    HeaDer,
    BackgroundEffect,
    AboutSeccion,

  },
  data() {
    return {

    }
  },

}
  //
</script>

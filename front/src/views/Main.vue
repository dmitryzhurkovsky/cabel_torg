<template>
  <div class="main">
    <Recomendation/>
    <Quick_category/>
    <News/>
    <Partners/>
    <About/>



  </div>
</template>

<script>
import About from '@/components/About/About.vue'
import Quick_category from '@/components/About/Quick_category.vue'
import Partners from "@/components/About/Partners.vue";
import News from "@/components/About/News.vue";
import Recomendation from "@/components/About/Recomendation.vue";
  export default {
    name: 'Main',

    components: {
      Recomendation,
      Partners,
  		About,
      Quick_category,
      News,

    },
  }
</script>

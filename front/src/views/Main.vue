<template>
  <div class="main">
    <Banner/>
    <Recomendation/>
    <Quick_category/>
    <News/>
    <Partners/>
    <About/>
    <Offer/>



  </div>
</template>

<script>
import Banner from '@/components/About/Banner.vue'
import About from '@/views/About.vue'
import Quick_category from '@/components/About/Quick_category.vue'
import Partners from "@/components/About/Partners.vue";
import News from "@/components/About/News.vue";
import Recomendation from "@/components/About/Recomendation.vue";
import Offer from "@/components/add_pages/offer_doc.vue";
  export default {
    name: 'Main',

    components: {
      Banner,
      Recomendation,
      Partners,
  		About,
      Quick_category,
      News,
      Offer

    },
  }
</script>

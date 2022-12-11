<template>
  <div class="main">
    <Banner/>
    <Recomendation/>
    <Quick_category/>
    <News/>
    <Partners/>
    <!-- <About/>
    <Offer/> -->



  </div>
</template>

<script>
import Banner from '@/components/about/Banner.vue'
// import About from '@/views/About.vue'
import Quick_category from '@/components/about/Quick_category.vue'
import Partners from "@/components/about/Partners.vue";
import News from "@/components/about/News.vue";
import Recomendation from "@/components/about/Recomendation.vue";
// import Offer from "@/components/add_pages/offer_doc.vue";

export default {
    name: 'Main',

    components: {
      Banner,
      Recomendation,
      Partners,
  		// About,
      Quick_category,
      News,
      // Offer

    },

    mounted(){
      this.$store.dispatch("breadcrumb/CHANGE_BREADCRUMB", 0);
    }
  }
</script>

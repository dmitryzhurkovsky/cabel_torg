<template>
  <div class="main" @click.stop = "SET_SEARCH_STRING('')">
    <Banner/>
    <Recomendation/>
    <Quick_category/>
    <News/>
    <Partners/>
    <About/>
    <!--<Offer/> -->



  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'
import Banner from '@/components/about/Banner.vue'
import About from '@/components/about/About_block_notuse.vue'
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
  		About,
      Quick_category,
      News,
      // Offer

    },

    methods:{
      ...mapMutations("query", ["SET_SEARCH_STRING"]),
      ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB"]),
    },

    mounted(){
      this.CHANGE_BREADCRUMB(0);
    }
  }
</script>

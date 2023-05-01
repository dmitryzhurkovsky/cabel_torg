<template>
  <div class="main" @click.stop = "SET_SEARCH_STRING('')">
    <SliderBanner />
    <!-- <SliderRecomendation /> -->
    <AboutQuickCategory />
    <SliderNews />
    <SliderPartners />
    <AboutInfo />
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
    name: 'Main',

    methods:{
      ...mapMutations("query", ["SET_SEARCH_STRING"]),
      ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB"]),
    },

    mounted(){
      this.CHANGE_BREADCRUMB(0);
    }
  }
</script>

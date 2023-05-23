<template>
  <div class="main" @click.stop = "SET_SEARCH_STRING('')">
    <SliderBanner />
    <SliderRecomendation 
      :isShowFilter = true
      :isShowFollow = true
    />
    <AboutQuickCategory />
    <SliderNews />
    <SliderPartners />
    <AboutInfo />
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

definePageMeta({
  // middleware: ["auth"],
  name: 'Главная',
});

export default defineNuxtComponent({
  name: 'Main',

  head () {
    return {
      title: 'Кабельторг | Купить  электротехническое оборудовение в Беларуси',
      meta: [{
        name: 'CabelTorg',
        content: 'Интернет магазин КабельТорг'
      }]
    }
  },

  methods:{
    ...mapMutations("query", ["SET_SEARCH_STRING"]),
    ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB"]),
  },

  mounted(){
    this.CHANGE_BREADCRUMB(0);
  }
})
</script>

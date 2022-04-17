<template>
  <div class="main">

    <Quick_category/>
    <Partners/>
    <About/>

  </div>
</template>

<script>
import About from '@/components/About/About.vue'
import Quick_category from '@/components/About/Quick_category.vue'
import Partners from "@/components/About/Partners.vue";
  export default {
    name: 'Main',

    components: {
      Partners,
  		About,
      Quick_category,

    },
  }
</script>

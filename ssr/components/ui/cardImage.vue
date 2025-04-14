<template>
    <img v-if = "images" 
      :class="[active === true ? 'active' : '']"
      :src=getImagePath(images) 
      :alt="alt"
    >
    <img v-else class="" src="@/assets/no_image.png" alt="">
</template>

<script>

export default {
  name: "CardImage",

  props: {
    images:  null,
    num: 0,
    active: false,
    alt: "",
  },

  methods:{
    getImagePath(item) {
      let itemNumber = 0;
      if (this.$props.num) itemNumber = this.$props.num;
      let path = null;
      if (item) {
        const allPath = item.split(',');
        path = useRuntimeConfig().public.NUXT_APP_IMAGES + allPath[itemNumber];
      }
      return path;
    },
  },
}
</script>

<style lang="scss" scoped>
img{
  max-width: 100%;
  max-height: 100%;
  //height: 100%;
  object-fit: contain;
}
.active {
  border: 2px solid blue;
}
</style>
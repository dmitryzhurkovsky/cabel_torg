<template>
      <img v-if = "images" class="" :src=getImagePath(images) alt="">
      <img v-if = "!images" class="" src="../../assets/no_image.png" alt="">
</template>

<script>

export default {
  name: "CardImage",

  props: {
    images:  null,
  },

  methods:{
    getImagePath(item) {
      let path = null;
      if (item) {
        const allPath = item.split(',');
        path = process.env.VUE_APP_IMAGES + allPath[0];
      }
      return path;
    },
  }
}
</script>

<style lang="scss" scoped>
img{
    max-width: 100%;
    max-height: 100%;
    height: 100%;
    object-fit: cover;
    width:100%;
    //max-height: 162px;
}

</style>
<template>
  <img v-if = "image" class="" :src=getImagePath(image) alt="">
  <img v-if = "!image" class="" src="../../assets/no_image.png" alt="">
</template>

<script setup lang="ts">

  const props = defineProps({
    image: {
      type: String,
      required: false,
      default: '',
    },
  })

  const getImagePath = (path: string) => {
    let imgPath = '';
    if (path) {
      imgPath = import.meta.env.VITE_APP_IMAGES + path;
    }
    return imgPath;
  }
</script>

<style lang="scss" scoped>
img{
max-width: 100%;
}

</style>
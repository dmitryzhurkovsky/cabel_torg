<template>
  <img v-if = "image" class="" :src=getImagePath(image) alt="">
  <img v-if = "!image" class="" src="../../assets/no_image.png" alt="">
</template>

<script setup lang="ts">
  import { onMounted } from "vue";

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
      const allPath = path.split(',');
      imgPath = import.meta.env.VITE_APP_IMAGES + allPath[0];
    }
    return imgPath;
  }

</script>

<style lang="scss" scoped>
  img{
    max-width: 100%;
  }

</style>
<template>
    <img v-if = "images" 
      :class="[active === true ? 'active' : '']"
      :src=getImagePath(images) 
      :alt="alt"
    >
    <img v-else class="" src="@/assets/no_image.png" alt="">
</template>

<script setup>

  const props = defineProps({
    images:  { type: String,  default: null},
    num:  { type: Number,  default: 0},
    active:  { type: Boolean,  default: false},
    alt:  { type: String,  default: ""},
  }); 

  const getImagePath = (item) => {
    let itemNumber = 0;
    if (props.num) itemNumber = props.num;
    let path = null;
    if (item) {
      const allPath = item.split(',');
      path = useRuntimeConfig().public.NUXT_APP_IMAGES + allPath[itemNumber];
    }
    return path;
  };
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
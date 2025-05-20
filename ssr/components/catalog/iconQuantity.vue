<template>
  <div class="icon-quantity" 
    v-if="quantity"
    :style = "{ left: left + 'px', top: top + 'px' }"
   >
    <div class="icon-quantity__info">{{ quantity }}</div>
  </div>
</template>

<script setup>

  const props = defineProps({
    quantity:  { type: Number,  default: 0},
    top:  { type: Number,  default: 10},
    left:  { type: Number,  default: 10},
  });

</script>

<style lang="scss" scoped>

.icon-quantity{
  display: flex;
  position: absolute;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  justify-content: center;
  align-items: center;
  background-color: #E30044;
  &__info {
    color: #FFFFFF;
    font-size: 10px;
  }
}
</style>

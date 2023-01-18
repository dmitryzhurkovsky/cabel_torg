<template>
      <div class="icon-quantity" 
        v-if="quantity"
        :style = "{ left: left + 'px', top: top + 'px' }"
       >
        <div class="icon-quantity__info">{{ quantity }}</div>
      </div>
</template>

<script>

export default {
  name: 'IconQuantity',

  props: {
    quantity:  0,
    top: 12,
    left: 12,
  },

}
</script>

<style lang="scss" scoped>

.icon-quantity{
  display: flex;
  position: absolute;
  // top: 12px;
  // left: 12px;
  width: 20px;
  height: 20px;
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

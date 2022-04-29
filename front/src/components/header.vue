<template>
  <header class="header">
      <div class="header__wrapper">
          <div class="header__content _container">
              <headerBody/>
              <headerTopMenu/>
          </div>

      </div>
  </header>
</template>

<script>

  import HeaderBody from '@/components/header/header-body.vue'
  import HeaderTopMenu from '@/components/header/header-topmenu.vue'

  export default {
    name: "Header",

    components:
    {
      HeaderBody, HeaderTopMenu,
    },
  }

</script>

<style scoped lang="scss">
.header {

    &__wrapper {
      padding: 24px 0;
      background: #F8FAFF;

    }

    &__container {
    }

    &__main {
    }

}

</style>

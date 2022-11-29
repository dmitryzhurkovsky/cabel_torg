<template>
  <div class="partners">
    <div class="partners__wrapper">
      <div class="partners__content _container">
        <div class="partners__body">

          <h3>Наши партнеры</h3>
          <div class="partners__items flex-center">
            <div class="parnters__item">
              <img src="../../assets/partners/11.png" alt="partners">
            </div>
            <div class="parnters__item">
              <img src="../../assets/partners/12.png" alt="partners">
            </div>
            <div class="parnters__item">
              <img src="../../assets/partners/13.png" alt="partners">
            </div>
            <div class="parnters__item">
              <img src="../../assets/partners/14.png" alt="partners">
            </div>
            <div class="parnters__item">
              <img src="../../assets/partners/12.png" alt="partners">
            </div>
            <div class="parnters__item">
              <img src="../../assets/partners/11.png" alt="partners">
            </div>
          </div>


        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'Partners',
  }
</script>

<style scoped lang="scss">

.partners {


  &__wrapper{
    padding: 20px 0;

  }
  &__content{

  }

  &__body{
    h3{
      text-align: center;
      margin-bottom: 36px;
    }
  }


  &__items{
  justify-content: space-around;
  }
  &__item{


  }
  &__link{

}

}

</style>
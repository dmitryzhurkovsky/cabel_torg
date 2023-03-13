<template>
  <div class="news">
    <div class="news__wrapper">
      <div class="news__content _container">
        <div class="news__body">
          <div class="news__block">
            <a class="news__item">
              <div class="_block">
                <img src="../assets/news/1.png" alt="">
              </div>
              <div class="_block">
                <div class="news__date">22.04.2022</div>
                <div class="news__title">Новый бренд</div>
                <div class="news__description">Высококлассное оборудование от Cisco уже в каталоге CabelTorg</div>

              </div>


            </a>
            <a class="news__item">
              <div class="_block">
                <img src="../assets/news/1.png" alt="">
              </div>
              <div class="_block">
                <div class="news__date">22.04.2022</div>
                <div class="news__title">Новый бренд</div>
                <div class="news__description">Высококлассное оборудование от Cisco уже в каталоге CabelTorg</div>

              </div>
            </a>


              <a class="news__item">
                <div class="_block">
                  <img src="../assets/news/1.png" alt="">
                </div>
                <div class="_block">
                  <div class="news__date">22.04.2022</div>
                  <div class="news__title">Новый бренд</div>
                  <div class="news__description">Высококлассное оборудование от Cisco уже в каталоге CabelTorg</div>

                </div>
              </a>


          </div>






        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'News',

    mounted(){
      this.$store.dispatch("breadcrumb/CHANGE_BREADCRUMB", 0);
      this.$store.commit('breadcrumb/ADD_BREADCRUMB', {
        name: this.$router.currentRoute.value.meta.name,
        path: this.$router.currentRoute.value.path,
        type: "global",
        class: ""
      });
    }
  }
</script>

<style scoped lang="scss">

.news {

  &__wrapper{


  }
  &__content{

  }

  &__body{


  }
  &__header{


  }
  &__block{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-column-gap: 20px;
    grid-row-gap: 20px;
    padding:20px 0 60px 0;

    @media (max-width: $md2+px) {
      grid-template-columns: repeat(1, 1fr);
    }

  }
  &__item{
    display: flex;
    align-items: flex-start;

    ._block{
      flex-basis: 50%;
    &:nth-child(1){
      img{
        width: 100%;
      }
    }
    &:nth-child(2){
      display: flex;
      flex-direction: column;
      padding: 20px 20px;
      @media (max-width: $md3+px) {
        padding: 0 20px 20px 20px;
      }
    }
    }

  }

  &__date{
    font-size: 14px;
    line-height: 130%;
    opacity: 0.4;
  }
  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    letter-spacing: 0.44px;
    margin: 16px 0;
  }

  &__description{
    font-size: 14px;
    line-height: 130%;
    opacity: 0.4;
  }


}


</style>

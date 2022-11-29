<template>
  <div class="news">
    <div class="news__wrapper">
      <div class="news__content _container">
        <div class="news__body">

          <h3>Новости CabelTorg</h3>
          <div class="news__block">
            <a class="news__item">
              <img src="../../assets/news/new1.png" alt="">
              <div class="news__title">Новый бренд!</div>
              <div class="news__desc">Высококлассное оборудование от Cisco уже в каталоге CabelTorg</div>
            </a>

            <a class="news__item">
              <img src="../../assets/news/new2.png" alt="">
              <div class="news__title">Большое поступление</div>
              <div class="news__desc">Более 1000 товарных новинок уже доступны для заказа!</div>
            </a>

            <a class="news__item">
              <img src="../../assets/news/new3.png" alt="">
              <div class="news__title">Февральские скидки!</div>
              <div class="news__desc">Не пропустите масштабную распродажу от CabelTorg</div>
            </a>

            <a class="news__item">
              <img src="../../assets/news/new1.png" alt="">
              <div class="news__title">Новый бренд!</div>
              <div class="news__desc">Высококлассное оборудование от Cisco уже в каталоге CabelTorg</div>
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
  }
</script>

<style scoped lang="scss">

.news {

  &__wrapper{
    padding: 20px 0;

  }
  &__content{

  }

  &__body{
    h3{
      margin-bottom: 20px ;
    }
  }

  &__block{
    display:grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows:auto;
    gap: 12px;
    width: 100%;
    @media (max-width: $md2+px) {
      grid-template-columns: repeat(2, 1fr);
    }

  }


  &__item{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-between;
    cursor: pointer;
    img{
      max-width: 100%;
    }

  }
  &__title{
    margin: 12px 0;
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    letter-spacing: 0.44px;
    color: $mainColor;
  }
  &__desc{
    font-size: 14px;
    line-height: 130%;
    color: $mainColor;
    opacity: 0.4;

  }


}

</style>
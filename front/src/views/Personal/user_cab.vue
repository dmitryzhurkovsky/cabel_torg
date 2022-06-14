<template>
  <div class="user-acc">
    <div class="user-acc__wrapper">
      <div class="user-acc__content _container">
        <div class="user-acc__body">

          <div class="user-acc__block">
<!--        # SIDEBAR-->
            <div class="user-acc__sidebar filter">
              <div class="filter__block">
                <div class="filter__box">
                  <div class="filter__title icon-arrow-up">Личный кабинет</div>

                  <ul class="filter__list">
                     <li class="filter__item icon-cart">Мои заказы</li>
                     <li class="filter__item icon-favorite-choosed">Избранные товары</li>
                     <li class="filter__item icon-setting">Настройки аккаунта</li>
                  </ul>
                  <hr class="hr">
                  <div class="icon-exit filter__item">Выйти из аккаунта</div>
                </div>

              </div>
            </div>
<!--        # CONTENT-->
            <div class="user-acc__content-block content-block">
                <OrderList/>
            </div>
            <div class="user-acc__content-block content-block">
                <FavoriteList/>
            </div>
            <div class="user-acc__content-block content-block">
                <!-- <OrderList/> -->
            </div>

          </div>




        </div>
      </div>
    </div>
  </div>
</template>

<script>

  import OrderList from '@/components/personal/order-list.vue';
  import FavoriteList from '@/components/personal/favorite-list.vue';

  export default {
    name: "personal",

    components:
    {
      OrderList, FavoriteList,
    },

    methods: {
    },
  }
</script>

<style scoped lang="scss">

.user-acc {

  &__wrapper{

  }

  &__body{
  }
  &__block{
    display: flex;
    align-items: flex-start;

  }
  &__sidebar{
    width: 270px;
  }


  &__item{

  }
  &__link{

}

}
.filter{

  &__block{

  }

  &__box{
    font-weight: 400;
    position: relative;

  }
  &__list{

  }
  .hr{
    height:2px;
    margin:24px 0 24px 0;
    background:#F0F0F1;
  }

  &__item{
    font-size: 14px;
    line-height: 24px;
    color: #423E48;
    margin-bottom: 8px;

    &:hover{
      color:#4275D8;
      cursor: pointer;
    }
    &:before{
      margin-right: 10px;
    }
  }

  &__title{
    background: #eceef1;
    padding: 6px 8px;
    font-weight: 500;
    font-size: 14px;
    line-height: 24px;
    color: #423E48;
    margin: 0 0 12px 0;
    &:before{
      position: absolute;
      top: 16px;
      right: 10px;
      font-size: 6px;
      //transform: rotate(-90deg);
    }
  }
  &__text{
    span{
      font-weight: 400;
      font-size: 14px;
      color: #423E48;
    }

  }

}


</style>

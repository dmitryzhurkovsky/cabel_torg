<template lang="html">
  <div class="header__topmenu topmenu flex-center">
    <div class="topmenu__left flex-center">
      <div class="burger-menu burger-menu--closed">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>


      <div class="topmenu__item"><a href="">Каталог товаров</a></div>
      <div class="topmenu__item"><a href="">Покупателям</a></div>
      <div class="topmenu__item"><a href="">О нас</a> </div>
    </div>

    <div class="topmenu__right flex-center">
      <div class="topmenu__item">
        <a href="">
          <img src="@/assets/svg/favorite.svg" alt="favorite">
        </a>

      </div>
      <div class="topmenu__item">
        <a href="">
          <img src="@/assets/svg/user.svg" alt="user">
        </a>

      </div>
      <div class="topmenu__item topmenu__cart">
        <a href="">
          <img src="@/assets/svg/cart.svg" alt="cart">
        </a>

      </div>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss" scoped>
.header {
    &__topmenu{
      padding: 20px 0;
      justify-content: space-between;
    }
}

.topmenu{

  &__item{
    padding: 0 10px 0 10px;
  }
  &__left{
    .topmenu__item{
      a{
        font-weight: 400;
        font-size: 16px;
        line-height: 19px;
        display: flex;
        align-items: center;
        color: #423E48;
      }

      &:nth-child(2){
        a{
          font-weight: 500;
          color: $secondColor;
        }


      }
      &:nth-child(3){
        border-left: 1px solid $mainColor;
        border-right: 1px solid $mainColor;

      }

    }

  }
  &__cart{

    &:after{
        content:"3";
        font-size:12px;
        color: #fff;
        background: red;
        border-radius:50%;
        padding: 0 4px;
        position:relative;
        left:-6px;
        top: 8px;
        opacity:0.9;
      }
    }

}

.menu{
    flex: 0 1 540px;
    &__body{
        @media (max-width: $md2+px) {
            position: fixed;
            width: 100%;
            //height: 100%;
            overflow: auto;
            top: -100%;
            left: 0;
            background-color: #07095E;
            transition: left 0.3s ease 0s;
            padding: 35px 15px 30px 15px;
            z-index: 2;
            &._active{
                top: 0;
            }

        }

    }
    &__list{
        margin-bottom:0;
        @media (min-width:$md2+px) {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-evenly;

        }
    }
    &__item{
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        padding: 5px 0;
        position: relative;
        // @include adaptiv-value("margin-right",35,5,1);
        margin-right: 35px;
        &:last-child{
            margin-right: 0;
        }
        @media (max-width:$md2+px) {
            margin-bottom: 20px;
        }

    }
    &__link{

        // @include adaptiv-font(14, 11, 14);
        font-weight: 600;
        text-transform: uppercase;
        transition: color 0.3s ease 0s;
        &:hover{
            transition: color 300ms ease-in-out;
        }

        @media (max-width: $md2+px){
            color: #fff;
        }
    }
}

//Burger
.burger-menu{
  margin: 0 auto;
  width: 24px;
  display: block;
  transition: all .3s;
  cursor: pointer;
  height: 24px;

  .bar{
    transition: all .3s;
    height: 2px;
    width: 100%;
    display: block;
    background-color: $secondColor;
    &:nth-of-type(2){
      margin: 5px 0;
    }
  }
  &--closed{
    transition-delay: .3s;
    .bar:nth-of-type(2){
      width: 75%;
      transition-property: margin, height, width;
      transition-delay: .3s, .3s, 0s;
    }
    .bar:nth-of-type(3) {
      width: 50%;
    }
    &:hover{
      .bar:nth-of-type(2){
        width: 100%;
      }
      .bar:nth-of-type(3){
        width: 100%;
      }

    }
    &--opened{
    padding-top: 12px;
    .bar:nth-of-type(1){
      transform: rotate(45deg);
      transition-delay: .3s;
      height: 2px;
    }

    .bar:nth-of-type(2){
      opacity: 0;
      height: 0;
      margin: -3px;
    }

    .bar:nth-of-type(3){
      transform: rotate(-45deg);
      transition-delay: .3s;
      height: 2px
    }
  }
  }
}


</style>

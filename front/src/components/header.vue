<template>
  <header class="header">
      <div class="header__wrapper">
          <div class="header__content _container">
              <div class="header__body">

                  <a href="/" class="header__logo">
                      <img src="../assets/logo.svg" alt="CabelTorg">
                  </a>
                  <div class="header__search search-wrapper">
                    <form>
                      <input type="text" name="focus" required class="search-box" placeholder="Поиск товаров" />
                      <button class="close-icon" type="reset"></button>
                    </form>
                  </div>
                  <div class="header__info info-header flex-center">
                        <div class="info-header__item">
                          <a href="tel:+375296889454">+375 29 688 94 54</a>
                        </div>
                        <div class="info-header__item">
                          <a href="mail:info@cabeltorg.by">info@cabeltorg.by</a>
                        </div>
                        <div class="info-header__item">BYN</div>
                  </div> <!--     header__main-->



              </div>  <!--header__body -->
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
                    <img src="../assets/svg/favorite.svg" alt="favorite">
                  </a>

                </div>
                <div class="topmenu__item">
                  <a href="">
                    <img src="../assets/svg/user.svg" alt="user">
                  </a>

                </div>
                <div class="topmenu__item topmenu__cart">
                  <a href="">
                    <img src="../assets/svg/cart.svg" alt="cart">
                  </a>

                </div>
              </div>



            </div>
          </div>

      </div>
  </header>
</template>

<script>
export default {
  name: "header"
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

    &__body {
      display: flex;
      align-items: center;
      justify-content: space-between;

    }

    &__search{
      //background: #FFFFFF;
      //box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
      //border-radius: 50px;
      //max-width: 384px;
      //height: 32px;
      //width: 100%;

    }
    &__info{
     justify-content: space-between;
    }

    &__main {


    }
  &__topmenu{
    padding: 20px 0;
    justify-content: space-between;
  }

    &__logo {


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

.info-header{

  &__item{
    padding: 0 20px 0 20px;
    &:nth-child(1){
      a{
        font-weight: 500;
        font-size: 14px;
        color: $mainColor;
      }

    }
    &:nth-child(2){
      border-left: 1px solid $mainColor;
      border-right: 1px solid $mainColor;
      a{
        font-weight: 300;
        text-decoration-line: underline;

      }

    }
    &:nth-child(3){

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


//SEARCH
.search-box,.close-icon,.search-wrapper {
  position: relative;
  padding: 10px;
}
.search-wrapper {

}
.search-box {
  background: #FFFFFF;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
  border-radius: 50px;
  max-width: 384px;
  width: 100%;
  font-size: 14px;
  opacity: 0.5;
  padding: 9px 16px;
  min-width: 300px;
}
.search-box:focus {
  border: 1px solid #bebede;
}
.close-icon {
  border:1px solid transparent;
  background-color: transparent;
  display: inline-block;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.close-icon:after {

}
.search-box:not(:valid) ~ .close-icon {
  display: none;
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


//==============big_header======================================================================================

//====================================================================================================


</style>

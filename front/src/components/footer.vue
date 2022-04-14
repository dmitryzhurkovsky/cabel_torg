<template>
  <footer class="footer">
      <div class="footer__wrapper">
          <div class="footer__content _container">
              <div class="footer__body">
                  <div class="footer__row flex-center">
                      <div class="footer__item">
                        <p>Остались вопросы?</p>
                        Напишите нам на почту <a href="mail:info@cabeltorg.by">info@cabeltorg.by</a>  или оставьте свой номер телефона и наш специалист вскоре свяжется с вами!
                      </div>
                      <button class="btn">Заказать звонок</button>
                  </div>

                <div class="footer__row flex-center">
                  <div class="footer__col">
                    <div class="footer__logo">
                      <img src="../assets/logo.svg" alt="CabelTorg">
                    </div>
                    <div class="footer__social social">
                      <div class="social__item"></div>
                      <div class="social__item"></div>
                      <div class="social__item"></div>
                    </div>

                  </div>
                  <div class="footer__col">
                    <div class="footer__item flex-center">
                      <img src="" alt="">
                      <a href="tel:+375296889454">+375 29 688 94 54</a>
                    </div>
                    <div class="footer__item flex-center">
                      <img src="" alt="">
                      <div>
                        <span>Адрес склада в Бресте:</span>
                        <span>225033, Брестская область,  а/г Большие Мотыкалы, ул. Центральная д.26А</span>
                      </div>
                    </div>
                    <div class="footer__item flex-center">
                      <img src="" alt="">
                      <div>
                        <span>Адрес склада в Минске:</span>
                        <span>Минск, Монтажников 3-й пер., 3</span>

                      </div>

                    </div>
                  </div>
                  <ul class="footer__col footer__menu">
                    <li class="footer__menu_link">О компании</li>
                    <li class="footer__menu_link">Контакты </li>
                    <li class="footer__menu_link">Оплата и доставка</li>
                    <li class="footer__menu_link">Оптовым покупателям</li>
                    <li class="footer__menu_link">
                      <a href="">Скачать прайс-лист</a>
                    </li>
                  </ul>

                  </div>
              </div>



          </div>
      </div>
    <div class="footer__down">
      <p>© cabeltorg.by - кабельная продукция. Все права защищены.</p>
      <p>Копирование информации с сайта запрещено.</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "footer"
}
</script>

<style scoped lang="scss">
.footer{

    &__wrapper{
    }
    &__content{}


    &__col{
      padding: 20px 20px 20px 0;

    }
    &__body{


    }

  &__row{
    &:nth-child(1){
      justify-content: space-between;
      border-bottom: 1px solid grey;
    }
  }
    &__item{

    }
    &__list{

    }


    &__logo{

    }
    &__social{

    &__link{
    }
    &__down{
      background: #423E48;
      p{
        font-weight: 300;
        font-size: 12px;
        line-height: 120%;
        color: #FFFFFF;
        opacity: 0.6;;
      }

    }


}

.social__block{

    }

}
//====================================================================================================

//====================================================================================================
.link__inside{

}

</style>

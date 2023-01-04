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
                     <li class="filter__item icon-order">Мои заказы</li>
                     <li class="filter__item icon-favorite">Избранные товары</li>
                     <li class="filter__item icon-setting">Настройки аккаунта</li>
                  </ul>
                  <hr class="hr">
                  <div class="icon-exit filter__item">Выйти из аккаунта</div>
                </div>

              </div>
            </div>
<!--        # CONTENT-->
            <div class="user-acc__content-block content-settings content-block">
              <div class="content-block__title">Ваши данные</div>
              <div class=" acc-settings">
                <div class="group">
                  <label for="user" class="label">Имя</label>
                  <div class="input__box">
                    <input id="user" type="text" class="input">
                    <i class="icon-pen input__icon"></i>
                  </div>


                </div>
                <div class="group__row flex-center">
                  <div class="group">
                    <label for="email" class="label">Электронная почта</label>
                    <div class="input__box">
                      <input id="email" type="text" class="input">
                      <i class="icon-pen input__icon"></i>
                    </div>
                  </div>
                  <div class="group">
                    <label for="phone" class="label">Номер телефона</label>
                    <div class="input__box">
                      <input id="phone" type="text" class="input">
                      <i class="icon-pen input__icon"></i>
                    </div>
                  </div>
                </div>
                <div class="group">
                  <label for="address" class="label">Адрес для доставки заказа</label>
                  <div class="input__box">
                    <input id="address" type="text" class="input">
                    <i class="icon-pen input__icon"></i>
                  </div>
                </div>

                <div class="group__row flex-center">
                  <div class="group">
                    <label for="pass" class="label">Пароль</label>
                    <div class="input__box">
                      <input id="pass" type="password" class="input" data-type="password">
                      <i class="icon-visible input__icon"></i>
                    </div>
                  </div>
                  <div class="popup__link foot-lnk">Изменить пароль</div>
                </div>

                <div class="group">
                  <label for="user" class="label">Название компании</label>
                  <div class="input__box">
                    <input id="address" type="text" class="input">
                    <i class="icon-pen input__icon"></i>
                  </div>
                </div>

                <div class="group">
                  <label for="user" class="label">УНП</label>
                  <div class="input__box">
                    <input id="address" type="text" class="input">
                    <i class="icon-pen input__icon"></i>
                  </div>
                </div>

                <div class="group">
                  <label for="user" class="label">Расчетный счет IBAN</label>
                  <div class="input__box">
                    <input id="address" type="text" class="input">
                    <i class="icon-pen input__icon"></i>
                  </div>
                </div>

                <div class="group">
                  <label for="user" class="label">Юридический адрес</label>
                  <div class="input__box">
                    <input id="address" type="text" class="input">
                    <i class="icon-pen input__icon"></i>
                  </div>
                </div>

                <div class="group">
                  <label for="user" class="label">БИК></label>
                  <div class="input__box">
                    <input id="address" type="text" class="input">
                    <i class="icon-pen input__icon"></i>
                  </div>
                </div>

                <div class="group">
                  <label for="user" class="label">Обслуживающий банк</label>
                  <div class="input__box">
                    <input id="address" type="text" class="input">
                    <i class="icon-pen input__icon"></i>
                  </div>
                </div>




                <div class="group">
                  <button type="submit" class="btn black">Сохранить изменения</button>
                </div>

              </div>
            </div>

          </div>




        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'user-cab-set',
  }
</script>

<style scoped lang="scss">

.user-acc {

  &__wrapper{

  }
  &__content-block{
    width: 100%;
    padding: 0 16px;
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


.content-block{
  &__title{
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    color: #423E48;
    margin-bottom: 40px;
  }
}
.order{

  &__list{

  }
  &__item{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 30px 18px 30px 28px;
    background: #FFFFFF;
    border: 2px solid #EEEEEE;
    border-radius: 8px;
    ._status-color{
      color: #32A071;
      font-weight: 500;
    }
  }
  &__num{
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    text-decoration-line: underline;
    color: #423E48;
    z-index: 4;
    &:hover{
      color: #4275D8;
      cursor: pointer;
    }
  }
  &__date{

  }

  &__delivery{

  }

  &__status{

  }



  &__price{
    font-weight: 500;
    span{
      font-weight: 400;
    }
  }
}

.content-settings{
  .acc-settings{
    text-align: center;
    margin: 0 auto;
  }

  h3{
    margin-bottom: 24px;
  }


  p{
    font-size: 14px;
    line-height: 140%;
    text-align: center;
    color: #423E48;
  }

  button{
    text-align: center;
  }
  .foot-lnk{
    font-size: 12px;
    text-align: center;
    text-decoration-line: underline;
    opacity: 0.6;
    width: 150px;
    &:hover{
      cursor: pointer;
      opacity: 1;
    }
  }
}
</style>

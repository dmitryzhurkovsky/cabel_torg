<template lang="html">
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
</template>

<script>
export default {
}
</script>

<style lang="scss" scoped>
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
    margin-bottom: 16px;
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

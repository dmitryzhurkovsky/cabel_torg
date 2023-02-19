<!--<template>-->
<!--  <div class="structure">-->
<!--    <div class="structure__wrapper">-->
<!--      <div class="structure__content _container">-->
<!--        <div class="structure__body">-->
<!--          <div class="structure__block">-->
<!--            <h3 class="structure__title">Доставка</h3>-->
<!--            <p class="structure__text">Для оптовых покупателей из РБ мы предлагаем несколько различных способов получения заказа:</p>-->
<!--            <li class="structure__list__item">Самовывоз со склада Брест с 09:00 до 18:00 (бесплатно)</li>-->
<!--            <li class="structure__list__item">Самовывоз со склада Минск с 09:00 до 18:00 (бесплатно)</li>-->
<!--            <li class="structure__list__item">Бесплатная доставка по РБ от 500 рублей (бесплатно)</li>-->
<!--            <li class="structure__list__item">Доставка по РБ  в любую точку (платно за счет клиента). Обсуждается индивидуально с менеджером.</li>-->
<!--            <h3  class="structure__title">Оплата</h3>-->
<!--            <p>Для оптовых покупателей из РБ доступен только безналичный расчет.</p>-->
<!--          </div>-->






<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<template>
  <div class="invoice__container _container">
      <div class="invoice__header">

        <img class="invoice__logo" src="@/assets/logo.svg" alt="">
        <div class="invoice__number">
          <span>Счет на оплату №</span>
          <span>Ввести номер счета</span>
          <span>от</span>
          <span>ДЕнь</span>
          <span>Месяц строчно</span>
          <span>Год</span>
        </div>
        <hr class="hr">
        <div class="invoice__supplier">
          <div>Поставщик</div>
          <div>ООО "КабельЭлектроТорг", УНП 291132270, Брестская область а-г Большие Мотыкалы, ул. Центральная д.26А, тел.: +375162545407, р/с
            BY75MMBN30125085100109330000 в банке ОАО "Банк Дабрабыт" БИК MMBNBY22 к/с 51</div>

        </div>
        <div class="invoice__customer">
          <div>Покупатель</div>
          <div> Данные покупателя с сайта</div>
      </div>
        <hr class="hr">
      </div>
      <div class="invoice__body">
      <!--  Table with all goods     -->
        <div class="invoice__table">
          <table>
            <tr>
              <td>№</td>
              <td>Товары (работы, услуги)</td>
              <td>Количество</td>
              <td>Ед. изм.</td>
              <td>Цена</td>
              <td>Стоимость</td>
              <td>Ставка НДС</td>
              <td>Сумма НДС</td>
              <td>Всего с НДС</td>
              <td>Вес</td>
            </tr>
            <tr>
              <td>1</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </table>
        </div>
        <div class="invoice__price">
          <div class="invoice__price__item">
            Сумма НДС: <span></span>
          </div>
          <div class="invoice__price__item"></div>
          Всего к оплате сумма с НДС: <span></span>
        </div>
        <hr class="hr">

      </div>
      <div class="invoice__footer">
        <div class="footer__dop-info">
          <p>Счет-фактура действует с даты ее подписания сторонами в течение всего срока договора поставки и является его неотъемлемой частью.</p>
          <p>Расчет за товар производится платежным поручением в порядке предварительной оплаты в течение 1 (Один) банковских дней с даты выставления счет-фактуры.</p>
          <p>Срок поставки в течение 14 (Четырнадцать) рабочих дней с даты получения предоплаты.</p>
          <p>Условия поставки: транспортом и за счет средств Поставщика.</p>
          <p>Данный счет является неотъемлемой частью договора Договор №  <span>Номер договра надо ввоодить</span></p>
          <p>В соответствии с требований постановления Министерства архитектуры и строительства Республики Беларусь от 30.07.2021 № 73 «О порядке регулирования цен на
            строительные материалы, изделия, конструкции» стороны пришли к соглашению, что поставляемый товар не должен использоваться при строительстве объектов (за
            исключением строительства автомобильных дорог, мостов и тоннелей), финансируемых полностью или частично за счет средств республиканского и (или) местных
            бюджетов, в том числе государственных целевых бюджетных фондов, а также государственных внебюджетных фондов, внешних государственных займов и внешних
            займов, привлеченных под гарантии Правительства Республики Беларусь, кредитов банков Республики Беларусь под гарантии Правительства Республики Беларусь и
            областных, Минского городского исполнительных комитетов, а также при строительстве жилых домов (за исключением финансируемых с использованием средств
            иностранных инвесторов). Покупатель в случае реализации поставляемого товара обязан совершить аналогичную оговорку. Поставщик не несет ответственность за
            нарушение Покупателем или иным третьим лицом условий использования товара. Причиненные Поставщику убытки вследствие нарушения условий использования
            товара подлежат возмещению Покупателем в полном объеме.</p>
        </div>
        <hr class="hr">
        <div class="footer__sign">

          <div>Руководитель</div>
          <div class="footer__sign__clm">
            <span>
              <img class="invoice__signature" src="@/assets/signature.png" alt="">
            </span>
            <span>подпись</span>
          </div>
          <div class="footer__sign__clm">
            <span>Петрошевич Р.Л.</span>
            <span>расшифровка подписи</span>
          </div>
        </div>

        <hr class="hr__dot">


        <div class="invoice__header">
          <div class="invoice__number text-center">
            <span>Протокол №</span>
            <span>Ввести номер счета</span>
            <span>от</span>
            <span>ДЕнь</span>
            <span>Месяц строчно</span>
            <span>Год</span>
          </div>
          <div class="text-center mb-20">согласования свободных отпускных цен на товары (продукцию)</div>
          <hr class="hr">
          <div class="invoice__supplier">
            <div>Поставщик</div>
            <div>ООО "КабельЭлектроТорг", УНП 291132270, Брестская область а-г Большие Мотыкалы, ул. Центральная д.26А, тел.: +375162545407, р/с
              BY75MMBN30125085100109330000 в банке ОАО "Банк Дабрабыт" БИК MMBNBY22 к/с 51</div>

          </div>
          <div class="invoice__customer">
            <div>Покупатель</div>
            <div> Данные покупателя с сайта</div>
          </div>
          <hr class="hr">
        </div>
        <div class="invoice__body">
          <!--  Table with all goods     -->
          <div class="invoice__table">
            <table>
              <tr>
                <td>№</td>
                <td>Наименование и краткая характеристика товара, артикул, марка, тип, сорт</td>
                <td>Объем партии</td>
                <td>Отпускная цена и (или) тариф по прейскуранту</td>
                <td>Размер предоставленной скидки</td>
                <td>СОтпускная цена и (или) тариф, применяемые в расчетах</td>
                <td>Вес</td>
              </tr>
              <tr>
                <td>1</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>

              </tr>
            </table>
          </div>
        </div>
        <div class="invoice__footer">
          <div class="footer__sign_btn">

            <div class="sign__item">Исполнитель(поставщик)
              <span></span>
              <div class="footer__sign__clm">
                <img class="invoice__signature" src="@/assets/signature.png" alt="">
                <img class="invoice__stamp" src="@/assets/stamp.png" alt="">
              </div>
            </div>

            <div class="sign__item">Покупатель
              <span></span>
            </div>
          </div>
          <div class="footer__address">
            <div>Адрес склада: 225033, Брестская область а-г Большие Мотыкалы, ул. Центральная д.26А</div>
            <div>Почтовый адрес: 224005, г. Брест, ул. ГОБК, 7, оф. 128</div>
            <div>Время работы: с 9.00 до 18.00, обеденный перерыв с 13.00 до 14.00 (понедельник – пятница)</div>
            <div>тел.+375(44)5751295 – Михаил (склад)</div>
            <div>тел. +375(33)9150035 - бухгалтерия</div>
          </div>

        </div>



      </div>
  </div>
</template>

<script>

  export default {
    name: 'Shipping',

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

<style lang="scss">

.structure {

  &__wrapper{


  }
  &__content{

  }

  &__body{


  }
  &__title{
   margin: 30px 0;

  }
  &__block{
    padding: 0px 0 60px 0;
    h3{


    }



  }

  &__list{
    &__item{
      line-height: 30px;
      &:last-child{
        margin-bottom: 30px;
      }

    }

  }

  &__text{
    font-weight: 300;
    font-size: 18px;
    line-height: 140%;
    color: #423E48;
    margin-bottom: 20px;

  }


}


</style>

<style>

.text-center{
  text-align: center;

}

.mb-20{
  margin-bottom: 20px;
}


.invoice__container{

  padding: 20px 0;
  position: relative;
  font-size: 14px;
}

.invoice__header div:nth-child(2){
  font-weight: 500;
}
.invoice__logo{
  position: absolute;
  right: 0;
  top: 0;
}

.invoice__number{
  width:100%;
  font-weight: 500;
  padding-bottom: 5px;

}
.invoice__number span{
  margin-right: 5px;

}

.invoice__supplier{
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin: 10px 0;
  font-weight: 500;
}
.invoice__supplier div:nth-child(1){
  font-weight: 300;
  padding-right: 20px;
}
.invoice__customer{
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin: 20px 0 10px 0;
  font-weight: 500;
}
.invoice__customer div:nth-child(1){
  font-weight: 300;
  padding-right: 20px;
}
.footer__dop-info{
  font-size: 10px;
  margin: 10px 0;
  line-height: 1.2;

}
.invoice__footer{

}

.footer__sign, .footer__sign_btn{
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 150px;
  padding: 10px 0;
}
.footer__sign_btn{
  height: 140px;
}
.footer__sign_btn .sign__item{
  position: relative;
}
.sign__item span{
  display: inline-block;
  width: 120px;
  border-bottom: 1px solid #000;

}
.invoice__signature{
  width: 140px;
  position: absolute;
  bottom: -45px;
  right: 0;
}

.invoice__stamp{
  width: 240px;
  position: absolute;
  top: -70px;
  right: -140px;
  opacity: 0.5;
}

.footer__sign__clm{

}

.footer__sign div:nth-child(1){
  font-weight: 500;
}
.footer__sign div:nth-child(2){
  position: relative;
  font-size: 10px;
  padding: 3px 30px;
  border-top: 1px solid #000;
  margin-top: 16px;

}
.footer__sign div:nth-child(3){
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 500;
}
.footer__sign div:nth-child(3) span:nth-child(2) {
  font-weight: 300;
  font-size: 10px;
  padding: 3px 10px;
  border-top: 1px solid #000;

}
.hr{
  height: 2px;
  background: #3c3f45;
}
.hr__dot{
  /*height: 2px;*/
  border-top: 1px dashed #3c3f45;
  margin: 30px 0;
}

.invoice__body{
  padding: 20px 0;
}
.invoice__table table{
  width: 100%;
}
.invoice__table td{
  font-weight: 500;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  font-size: 12px;
  text-align: center;
  padding: 5px 2px;
}
.invoice__table td{}

.invoice__price{
  padding: 20px 0;
  font-size: 13px;

}
.invoice__price__item{
  font-weight: 500;
}

.invoice__price__item:nth-child(2){
  font-weight: 500;
  margin-top: 10px;
}

.footer__address{
  font-size: 12px;
  text-align: center;
  padding: 10px 0;
  line-height: 1.2;
}
.footer__address div:nth-child(1){
  font-weight: 500;
}


</style>

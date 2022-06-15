<template>
  <div class="about">
    <div class="about__wrapper">
      <div class="about__content _container">
        <div class="about__body">
          <div class="about__header">
            <h3>Информация о компании</h3>
            <p><b>Компания Cabel Torg</b> - это открытый и честный магазин, который помогает IT и
              Телеком отрасли в решении задач по выбору и поставке оборудования.</p>
            <div class="about__block">
              <div class="about__block__item">
                <div class="about__block__icon">
                  <img src="../assets/svg/1.svg" alt="">
                </div>
                <div class="about__block__text">Высокое качество товаров</div>
              </div>
              <div class="about__block__item">
                <div class="about__block__icon">
                  <img src="../assets/svg/2.svg" alt="">
                </div>
                <div class="about__block__text">Быстрое реагирование и отличный сервис</div>
              </div>
              <div class="about__block__item">
                <div class="about__block__icon _icon-quality">
                  <img src="../assets/svg/3.svg" alt="">
                </div>
                <div class="about__block__text">1000+ наименований в каталоге</div>
              </div>
            </div> <!--   about__block-->
          </div>

            <div class="about__paragraph">
              <div class="about__paragraph__title">
                <span>Наши услуги</span>
              </div>
              <div class="about__paragraph__text">
                <p>Наша компания осуществляет продажу кабельно-проводниковой, а также  электротехнической продукции на белорусский рынок.  Сегодня наш ассортимент насчитывает несколько сотен наименований известных отечественных и зарубежных производителей.</p>
                <p>Среди прочих товарных позиций мы реализуем кабеля и кабельную продукцию, сетевое оборудование, оптические компоненты, оборудование для сварки, оптических волокон, телевидение, системы видеонаблюдения</p>

              </div>
            </div>
          <div class="about__paragraph">
            <div class="about__paragraph__title">
              <span>Наши цели</span>
            </div>
            <div class="about__paragraph__text">
              <p>Мы всегда нацелены на установление и поддержание взаимовыгодных отношений с нашими клиентами и партнерами. Наша компания была основана в 2011 году. За период ее существования  мы создали предприятие, способное успешно взаимодействовать с клиентами и достойно выстраивать отношения с конкурентами. Приоритетом для нас также является развитие на рынке в целом, расширение географии поставок.</p>

            </div>
          </div>

          <div class="about__paragraph">
            <div class="about__paragraph__title">
              <span>Реквизиты компании</span>
            </div>
            <div class="about__paragraph__text">
              <p class="text_paragraph__item">ООО «КабельЭлектроТорг»</p>
              <p class="text_paragraph__item">УНП 291132270</p>
              <p class="text_paragraph__item"> ОКПО 302938961000</p>
              <br>
              <p class="text_paragraph__item"><b>Юр. адрес:</b> 225033, Брестская область, а-г Большие Мотыкалы, ул. Центральная д.26А</p>
              <p class="text_paragraph__item"><b>Почтовый адрес:</b> 224005, г. Брест, ул. ГОБК, 7, оф. 128</p>
              <p class="text_paragraph__item"><b>Тел/факс:</b> +375 162 54-54-07</p>
              <br>
              <p class="text_paragraph__item"><b>Банк:</b> Открытое акционерное общество "Банк Дабрабыт"</p>
              <p class="text_paragraph__item"><b>р/с в формате IBAN:</b> BY75MMBN30125085100109330000</p>
              <p class="text_paragraph__item"><b>(RUR)</b> BY32MMBN30125000001100466382</p>
              <p class="text_paragraph__item">ОАО «Банк Дабрабыт»</p>
              <br>
              <p class="text_paragraph__item"><b>Директор:</b> Петрошевич Роман</p>
            </div>
          </div>

          <div class="about__paragraph rectangle__text">
            <p>Выбирайте нас!</p>
            <p>Ведь сотрудничая с нами, Вы сможете оперативно решать вопросы снабжения продукцией высокого качества по реальным ценам. С нами удобно работать:
            </p>
            <li class="rectangle__text__item">наличие постоянного ассортимента продукции на собственном складе сокращает сроки исполнения Вашего заказа;</li>
            <li class="rectangle__text__item">доставку товара мы осуществляем в точно согласованные сроки;</li>
            <li class="rectangle__text__item">гибкая система скидок в зависимости от объема партии, сроков оплаты и условий доставки позволит Вам самостоятельно выбрать для себя оптимальные условия сотрудничества;</li>
            <li class="rectangle__text__item">у нас принципиально высокие требования к качеству поставляемой продукции, наличие сертификатов соответствия, протоколов испытаний, подтверждающих качество предлагаемого товара, и сопроводительных документов, позволяющих установить производителя – все это позволит Вам избежать неприятных последствий.</li>
          </div>



        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'About',

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

.about {

  &__wrapper{


  }
  &__content{

  }

  &__body{
    background-image: url("../assets/about-bg.png");
    background-repeat: no-repeat;
    background-position: top right;

  }
  &__header{

    p{
      font-size: 18px;
      line-height: 140%;
      margin: 30px 0 40px 0;
      width:50%;
      text-align: left;
      @media (max-width: $md3+px) {
        width:100%;
      }

    };


  }
  &__block{
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
    margin: 60px 0;
    @media (max-width: $md3+px) {
     flex-direction: column;
    }


    &__icon{
      margin-bottom: 22px;
      @media (max-width: $md3+px) {
        margin-bottom: 0;
      }
    }


    &__item{
      background: #FFFFFF;
      border: 2px solid #EEEEEE;
      box-sizing: border-box;
      border-radius: 8px;
      margin: 0 16px 8px 0;
      padding: 24px 24px;
      max-width: 272px;

      &:last-child{
        margin: 0 0px 8px 0;
      }
      @media (max-width: $md3+px) {
        max-width: 100%;
        width: 100%;
        display: flex;
        align-items: center;
      }


    }
    &__text{
      font-size: 18px;
      line-height: 24px;
      color: #423E48;
      @media (max-width: $md2+px) {
        padding-left: 20px;
      }
    }
  }
  &__paragraph{
    margin-bottom: 60px;

    &__title{
      position: relative;
      height: 20px;
      background: rgba(66, 117, 216, 0.1);
      border-radius: 4px;
      span{

        font-weight: 500;
        position: absolute;
        top: -10px;
        left: 10px;
        font-size: 20px;
        line-height: 24px;
        color: #4275D8;
      }


    }
    &__text{

      p{
        margin: 10px 0;
        font-size: 18px;
        line-height: 140%;
      }
    }
  }
  .rectangle__text{
    background: #FFFFFF;
    border: 2px solid #EEEEEE;
    box-sizing: border-box;
    border-radius: 8px;
    padding: 38px 28px 48px 28px;
    font-size: 18px;
    line-height: 140%;
    @media (max-width: $md3+px) {
      padding: 20px 12px 30px 12px;
    }

    p{
      margin-bottom: 20px;
      &:first-child{
        font-size: 20px;
        font-weight: bold;

        line-height: 24px;
        text-align: center;
        color: #423E48;
        text-align: center;
      }
    }

    &__item{
      padding-left: 20px;



    }

  }
}

</style>

<template>
  <Breadcrumb/>
  <div class="about app__content">
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
                  <img src="@/assets/svg/1.svg" alt="">
                </div>
                <div class="about__block__text">Высокое качество товаров</div>
              </div>
              <div class="about__block__item">
                <div class="about__block__icon">
                  <img src="@/assets/svg/2.svg" alt="">
                </div>
                <div class="about__block__text">Быстрое реагирование и отличный сервис</div>
              </div>
              <div class="about__block__item">
                <div class="about__block__icon _icon-quality">
                  <img src="@/assets/svg/3.svg" alt="">
                </div>
                <div class="about__block__text">1000+ наименований в каталоге</div>
              </div>
            </div>
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
              <p class="text_paragraph__item">УНП {{ settings.unp }}</p>
              <p class="text_paragraph__item"> ОКПО {{ settings.OKPO }}</p>
              <br>
              <p class="text_paragraph__item"><b>Юр. адрес:</b> {{ settings.legal_address }}</p>
              <p class="text_paragraph__item"><b>Почтовый адрес:</b> {{ settings.postal_address }}</p>
              <p class="text_paragraph__item"><b>Тел/факс:</b> {{ settings.phone_and_fax }}</p>
              <br>
              <p class="text_paragraph__item"><b>Банк:</b> {{ settings.serving_bank }}</p>
              <p class="text_paragraph__item"><b>р/с в формате IBAN:</b> {{ settings.IBAN }}</p>
              <p class="text_paragraph__item">{{ settings.serving_bank_short }}</p>
              <br>
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

<script setup>
  import { useHead } from 'nuxt/app';
  import { useMainStore } from '@/stores/main';
  import { onMounted } from 'vue';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const router = useRouter();
  const route = useRoute();
  const config = useRuntimeConfig();

  const mainStore = useMainStore();
  const breadCrumbStore = useBreadCrumbStore();

  const { settings } = storeToRefs(mainStore);

  const createCanonicalLink = computed(() => {
    return config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + route.path;
  });

  useHead({
    title: 'Кабельторг | О компании',
    meta: [{
      name: 'О компании',
      content: 'Страница о компании'
    }],
    link: [
      { rel: 'canonical', href: createCanonicalLink.value },
    ],
  });

  onMounted(() => {
    breadCrumbStore.changeBreadCrumb(0);
    breadCrumbStore.addBreadCrumb({
      name: "О Компании",
      path: router.currentRoute.value.path,
      type: "global",
      class: ""
    });
  });

</script>

<style scoped lang="scss">

.about {

  &__body{
    background-image: url("@/assets/about-bg.png");
    background-repeat: no-repeat;
    background-position: top right;
    @media (max-width: $md2+px) {
      background-size:50%;
    }
    @media (max-width: $md3+px) {
      background-image: none;
    }

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
    display: grid;
    grid-template-columns: repeat(3, 270px);
    gap: 10px;
    margin: 60px 0;
    @media (max-width: $md2+px) {
      grid-template-columns: repeat(2, minmax(200px, auto));
    }
    @media (max-width: $md3+px) {
      grid-template-columns: 1fr;
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
      width: 270px;
      max-width: 100%;

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
      @media (max-width: $md3+px) {
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

<template>
  <footer class="footer" v-if = "settings">
      <div class="footer__wrapper">
          <div class="footer__content _container">
              <div class="footer__body">
                  <div class="footer__row flex-center">
                      <div class="footer__item">
                        <h3>Остались вопросы?</h3>
                        <p>Напишите нам на почту <a class="_link" :href = "'mailto:' + settings.email">{{ settings.email }}</a>  или оставьте свой номер телефона и наш специалист вскоре свяжется с вами!</p>
                      </div>
                      <button class="btn" @click.stop = "onMadeCall(true)">Заказать звонок</button>
                  </div>
                  <div class="footer__row flex-center">

                    <div class="footer__col footer__subrow">
                      <div class="footer__logo">
                        <img src="@/assets/logo.svg" alt="CabelTorg">
                      </div>
                      <div class="footer__social social">
                        <!-- <a :href = settings.instagram_url class="social__item icon-instagram" target="_blank"></a>
                        <a :href = settings.vk_url class="social__item icon-vk" target="_blank"></a>
                        <a :href = settings.facebook_url class="social__item icon-facebook" target="_blank"></a> -->

                        <a :href = settings.telegram_url class="social__item" target="_blank">
                         <img src="@/assets/svg/telegram.svg" alt="Telegram">
                        </a>
                        <a :href = settings.vk_url class="social__item" target="_blank">
                         <img src="@/assets/svg/viber.svg" alt="Viber">
                        </a>
                      </div>
                    </div>
                    <div class="footer__subrow">
                      <div class="footer__col">
                        <div class="footer__item flex-center icon-phone">
                          <a class="_title" :href="'tel:' + String(settings.phone).replace(/ /g,'')">{{ settings.phone }}</a>
                        </div>
                        <div class="footer__item flex-center icon-place" 
                          v-for = "address in settings.addresses" 
                          :key ="address.id"
                        >
                          <div>
                            <div class="_title">{{ address.title }}:</div>
                            <div>{{ address.payload }}</div>
                          </div>
                        </div>
                      </div>
                      <ul class="footer__col footer__menu">
                        <li @click = "linkClick('/about')" class="footer__menu_link">
                          <span>О компании</span>
                        </li>
                        <li @click = "linkClick('/contacts')" class="footer__menu_link">
                          <span>Контакты</span>
                        </li>
                        <li @click = "linkClick('/shipping')" class="footer__menu_link">
                          <span>Оплата и доставка</span>
                        </li>
                        <li @click = "linkClick('/how_to_work')" class="footer__menu_link">
                          <span>Оптовым покупателям</span>
                        </li>
                        <li @click = "downLoadPrice" class="footer__menu_link">
                          <span >Скачать прайс-лист</span>
                        </li>
                      </ul>
                    </div>
                  </div>
              </div>
          </div>
      </div>
      <div class="footer__down">
        <div class="_container">
          <p>© cabel-torg.by - кабельная продукция. Все права защищены.</p>
          <p>Копирование информации с сайта запрещено.</p>
        </div>

      </div>
  </footer>
</template>

<script setup>
  import { useNotificationsStore } from '@/stores/notifications';
  import { useMainStore } from '@/stores/main';
  import { useHeaderStore } from '@/stores/header';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';
  
  const route = useRoute();
  const router = useRouter();

  const notificationsStore = useNotificationsStore();
  const mainStore = useMainStore();
  const headerStore = useHeaderStore();
  const breadCrumbStore = useBreadCrumbStore();

  const { settings } = storeToRefs(mainStore);

  const linkClick = (URL, name) => {
    if (route.path != URL) {
        breadCrumbStore.changeBreadCrumb(0);
        breadCrumbStore.addBreadCrumb({name: name, path: URL, type: "global", class: ""});
        router.push(URL);
    }
  };

  const downLoadPrice = () => {
    notificationsStore.setIsLoading(true);
    const _url = useRuntimeConfig().public.NUXT_APP_IMAGES + settings.price_document;
    window.open(_url, '_blank');
    notificationsStore.setIsLoading(false);
  };

  const onMadeCall = (status) => {
    headerStore.setIsPopUpOpen(status)
    headerStore.setRequestCallType('U');
    headerStore.setPopUpAction('RequestCall');
  };
</script>

<style lang="scss">
.footer{

&__wrapper{
  background-color:#F4F5F8;
}
&__down{
  background: #423E48;
  padding: 21px 0;
  p{
    font-weight: 300;
    font-size: 12px;
    line-height: 120%;
    color: #FFFFFF;
    opacity: 0.6;;
  }
}
&__content{}


&__col{}

&__body{}

&__row{
&:nth-child(1){
  justify-content: space-between;
  border-bottom: 1px solid rgba(66, 62, 72, 0.2);
  //@include adaptiv-value("padding-top",28,20,28);
  //@include adaptiv-value("padding-bottom",28,20,28);
  padding: 28px 0;

  @media (max-width: $md2 + px) {
    flex-direction: column;
    align-items: flex-start;
    padding: 24px 0;
  }
  h3{
    font-size: 16px;
    margin-bottom: 3px;
    letter-spacing: 0.44px;
  }
  p{
    font-weight: 300;
    font-size: 14px;
    line-height: 130%;
    color: #000000;
    @media (max-width: $md2+px) {
      margin-bottom: 20px;
    }
  }
}
&:nth-child(2){
  justify-content: space-between;

  @media (max-width: $md2+px) {
    flex-direction: column;
    align-items: flex-start;
  }
  .footer__col{
    &:nth-child(1){
      padding-right: 20px;

      @media (max-width: $md2+px) {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        padding-right: 0;
        //border-bottom: 1px solid rgba(66, 62, 72, 0.2);
      }
    }

    &:nth-child(2){
      //padding: 0 10px 0 20px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: space-between;
    }
    &:nth-child(3){
      padding: 0 0 0 20px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: space-between;
    }
  }

}


}

&__subrow{
&:nth-child(1){
  @media (max-width: $md2+px) {
    padding: 24px 0;
    border-bottom: 1px solid rgba(66, 62, 72, 0.2);
  }



}





&:nth-child(2){
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 0;
  .footer__col:nth-child(1){
    flex-direction: column;
    align-items: flex-start;
    flex-basis: 70%;
    @media (max-width: $md2+px) {


    }
    @media (max-width: $md3+px) {
      border-bottom: 1px solid rgba(66, 62, 72, 0.2);
      //border-top: 1px solid rgba(66, 62, 72, 0.2);
      padding-bottom: 20px;
      //padding: 20px 0;
    }


  }
  .footer__col:nth-child(2){
    @media (max-width: $md3+px) {
      padding: 20px 0;
    }
    flex-basis: 30%;

  }
  @media (max-width: $md3+px) {
    flex-direction: column;
    align-items: flex-start;
  }

}
}
&__item{
  padding: 5px 5px 5px 0;
  align-items: flex-start;

  &:before{
    margin-right: 10px;
    font-size: 20px;
  }
}
&__list{

}
&__menu{

&_link{
  padding: 5px 0;


  span{
    font-weight: 300;
    font-size: 14px;
    line-height: 14px;
    color: #423E48;
    cursor: pointer;
    transition: all 0.3s ease;
    &:hover{
      color:#4275D8;
    }
  }

}

}


&__logo{

  border-bottom: 1px solid rgba(66, 62, 72, 0.2);
  padding: 0 0 20px 0;
  @media (max-width: $md2+px) {
    border-bottom: none;
    padding: 0 0 0 0;
  }


}
&__social{
  display: flex;
  justify-content: space-between;
  padding: 20px 0 20px 0;
  @media (max-width: $md2+px) {
    gap:10px;
    padding: 0 0 0 0;
  }

&__link{
}


}

.social{

&__item{
font-size: 30px;
color: #423E48;
opacity: 0.3;
transition: all 0.3s ease;
&:hover{
  color: #4275D8;
  opacity: 1;
}
//margin: 0 5px;
&:last-child{
}
}
}

}
//====================================================================================================

//====================================================================================================
.link__inside{

}

</style>

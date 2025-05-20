<template>
  <div class="wholesale app__content">
    <div class="wholesale__wrapper">
      <div class="wholesale__content _container">
        <div class="wholesale__body">
          <div class="wholesale__block flex-center">
            <div class="wholesale__item _block">
              <h3>Информация для оптовых клиентов</h3>
              <p>Организация СabelTorg занимается реализацией кабельной продукции на всей территории Республики Беларусь.</p>
              <p>Наличие складов в Минске и Бресте позволяет оперативно осуществлять доставку в любую точку страны. А при покупке от 300 бел. рублей, доставка будет для Вас бесплатной!</p>
              <p>Мы являемся первыми импортерами в РБ. Продукция почти всегда в наличии на складе или может быть пополнена за короткий промежуток времени.</p>
              <a class="btn wholesale__btn" :href="'tel:' + String(settings.phone).replace(/ /g,'')">Позвонить</a>
            </div>

            <div class="wholesale__item _block">
              <img src="@/assets/sertificate.svg" alt="Сертификат">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useHead } from 'nuxt/app';
  import { onMounted } from 'vue';
  import { useMainStore } from '@/stores/main';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const router = useRouter();

  const mainStore = useMainStore();
  const breadCrumbStore = useBreadCrumbStore();

  const { settings } = storeToRefs(mainStore);

  useHead({
    title: 'Кабельторг | Оптовым клиентам',
    meta: [{
      name: 'Оптовым клиентам',
      content: 'Страница Оптовым клиентам'
    }]
  });

  onMounted(() => {
    breadCrumbStore.changeBreadCrumb(0);
    breadCrumbStore.addBreadCrumb({
      name: router.currentRoute.value.meta.name,
      path: router.currentRoute.value.path,
      type: "global",
      class: ""
    });
  })
</script>

<style scoped lang="scss">

.wholesale {

  &__block{
    align-items: flex-start;
    padding: 20px 0 30px 0;
    @media (max-width: $md2+px) {
     flex-direction: column;
      &:nth-child(2){
        text-align: center;
      }
    }

    h3 {
      margin-bottom: 30px;
    }
    p{
      margin: 10px 0;
      font-weight: 300;
      font-size: 18px;
      line-height: 140%;
    }
    button{
      margin-top: 40px;
    }
  }
  &__item{
    flex-basis: 50%;
    width: 100%;
    &:nth-child(1){
      @media (max-width: $md3+px) {
        margin-bottom: 20px;
      }
    }
    img{
      max-width: 100%;
    }
  }

  &__btn{
    margin: 20px 0;
    display: block;
    width: 200px;
  }
}


</style>

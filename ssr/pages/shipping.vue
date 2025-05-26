<template>
  <Breadcrumb/>
  <div class="structure app__content">
    <div class="structure__wrapper">
      <div class="structure__content _container">
        <div class="structure__body">
          <div class="structure__block">
            <h3 class="structure__title">Доставка</h3>
            <p class="structure__text">Для оптовых покупателей из РБ мы предлагаем несколько различных способов получения заказа:</p>
            <li 
              class="structure__list__item" 
              v-for = "delivery in deliveryTypes" 
              :key = delivery.id 
            >
              {{ delivery.payload }}
            </li>
            <h3  class="structure__title">Оплата</h3>
            <p>Для оптовых покупателей из РБ доступен только безналичный расчет.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useHead } from 'nuxt/app';
  import { onMounted } from 'vue';
  import { useOrdersStore } from '@/stores/orders';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const router = useRouter();
  const route = useRoute();
  const config = useRuntimeConfig();

  const oredersStore = useOrdersStore();
  const breadCrumbStore = useBreadCrumbStore();

  const { deliveryTypes } = storeToRefs(oredersStore);

  const createCanonicalLink = computed(() => {
    return config.public.NUXT_APP_DOCUMENTS.slice(0, -1) + route.path;
  });

  useHead({
    title: 'Кабельторг | Оплата и доставка',
    meta: [{
      name: 'Оплата и доставка',
      content: 'Страница Оплата и доставка'
    }],
    link: [
      { rel: 'canonical', href: createCanonicalLink.value },
    ],
  });

  onMounted(() => {
    breadCrumbStore.changeBreadCrumb(0);
    breadCrumbStore.addBreadCrumb({
      name: "Оплата и доставка",
      path: router.currentRoute.value.path,
      type: "global",
      class: ""
    });
  });
</script>

<style lang="scss">

.structure {

  &__title{
   margin: 30px 0;

  }
  &__block{
    padding: 0px 0 60px 0;
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

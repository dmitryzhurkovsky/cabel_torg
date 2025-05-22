<template>
  <Breadcrumb/>
  <div class="structure app__content">
    <div class="structure__wrapper">
      <div class="structure__content _container">
        <div class="structure__body">
          <div class="structure__block">
            <h3 class="structure__title">Как совершить покупку?</h3>
            <ol>
              <li class="structure__list__item">Воспользуйтесь поиском или навигацией по каталогу, чтобы выбрать интересующий вас товар.
                (Если нужного вам товара нет на складе или в каталоге, вы можете отправить запрос на контактную почту <a class="_link" href="/">info@cabeltorg.by</a> с указанием наименования, модели и производителя товара, после чего с вами свяжется наш менеджер).</li>

              <li class="structure__list__item">При помощи кнопки «В корзину» добавьте нужные товары к заказу. Корзина всегда доступна для просмотра с каждой страницы магазина, и Вы в любой момент можете приступить к оформлению заказа. В корзине можно легко исправить состав заказа: удалить ненужные товары или изменить их количество.</li>

              <li class="structure__list__item">Оформление заказа происходит в несколько шагов посредством заполнения несложной формы. Обратите внимание на поля, обязательные для заполнения: эти сведения нужны для правильного оформления Вашего заказа и его оперативной доставки.</li>

              <li class="structure__list__item">Получив заказ, наш оператор свяжется с Вами по указанному телефону для подтверждения принятой информации и уточнения срока доставки.
                Так же наш оператор выставит Вам счет за выбранные товары, который будет действителен в течение трех банковских дней. Сразу же после оплаты счета, заказ можно будет забрать со склада (при оформлении самовывоза), или Ваш товар будет отправлен курьером по указанному адресу.</li>
            </ol>
            <p class="structure__text">Подробнее о способах доставки и оплаты товаров — в разделе <a class="_link" href="/shipping">«Доставка и  оплата»</a>.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { useHead } from 'nuxt/app';
  import { onMounted } from 'vue';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const router = useRouter();

  const breadCrumbStore = useBreadCrumbStore();

  useHead({
    title: 'Кабельторг | Как оформить заказ',
    meta: [{
      name: 'Как оформить заказ',
      content: 'Страница Как оформить заказ'
    }]
  });

  onMounted(() => {
    breadCrumbStore.changeBreadCrumb(0);
    breadCrumbStore.addBreadCrumb({
      name: "Оформление заказа",
      path: router.currentRoute.value.path,
      type: "global",
      class: ""
    });
  })
</script>

<style scoped lang="scss">

.structure {

  &__wrapper{


  }
  &__content{

  }

  &__body{


  }
  ol {
    list-style: decimal;
    padding-left: 24px;

  }
  ol li {
    padding-left: 24px;
    margin-bottom: 28px;

  }
  ol li::marker {

    font-weight: 500;
    font-size: 22px;
    color: #423E48;


  }

  &__block{


  }
  &__text{
    font-weight: 400;
    font-size: 18px;
    line-height: 120%;
    color: #423E48;
  }


}


</style>

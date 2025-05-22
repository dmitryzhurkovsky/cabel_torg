<template>
  <Breadcrumb/>
  <div class="structure app__content">
    <div class="structure__wrapper">
      <div class="structure__content _container">
        <div class="structure__body">
          <div class="structure__block">

            <h3 class="structure__title">Гарантия</h3>
            <p class="structure__text">На всю продукцию распространяется гарантия завода-изготовителя (12-24 месяца), при условии соблюдения правил транспортировки, хранения, прокладки и эксплуатации.</p>
            <p class="structure__text">Вся поставляемая нами продукция соответствует требованиям технического регламента Таможенного союза и нормативных документов (ГОСТ, ТУ), что подтверждается необходимыми сертификатами и паспортами качества действующими на территории РБ.</p>
            <p class="structure__text">Согласно Постановлению Совета Министров РБ №778 от 14.06.2002г. <span class="_bold">ПРОВОДА, ШНУРЫ, КАБЕЛИ обмену и возврату не подлежат</span>.</p>
            <p class="structure__text">Выдержки из законодательных актов: Перечень непродовольственных товаров надлежащего качества, не подлежащих обмену, утвержденный постановлением Совета Министров Республики Беларусь от 14 июня 2002 г. № 778, разработан во исполнение статьи 26 Закона Республики Беларусь «О защите прав потребителей».</p>
            <p class="structure__text">Согласно статье 26 Закона законодатель определил перечень доброкачественных товаров, которые обмену и возврату не подлежат: метражные товары (ткани из волокон всех видов, трикотажное и гардинное полотно, мех искусственный, ковровые изделия, нетканые материалы, ленты, кружево, тесьма, <span class="_bold">ПРОВОДА, ШНУРЫ, КАБЕЛИ</span>, линолеум, багет, пленка, клеенка и др.)</p>
            <p class="structure__text _bold">Возврат денег за отрезанную продукцию <span>НЕ ПРОИЗВОДИТСЯ</span></p>.

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
    title: 'Кабельторг | Гарантия',
    meta: [{
      name: 'Гарантия',
      content: 'Страница Гарантия'
    }]
  });

  onMounted(() => {
    breadCrumbStore.changeBreadCrumb(0);
    breadCrumbStore.addBreadCrumb({
      name: "Гарантии",
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
  &__header{


  }
  &__text{

    ._bold{
      font-weight: 500;
    }

  }
  &__item{

  }

}

</style>

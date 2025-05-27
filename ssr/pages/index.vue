<template>
  <div class="main" @click.stop = "queryStore.setSearchString('')">
    <SliderBanner />
    <!-- <ClientOnly> -->
      <SliderRecomendation 
        :isShowFilter = true
        :isShowFollow = true
      />
    <!-- </ClientOnly> -->
    <AboutQuickCategory />
    <SliderNews />
    <SliderPartners />
    <AboutInfo />
  </div>
</template>

<script setup>
  import { useHead } from 'nuxt/app';
  import { onMounted } from 'vue';
  import { useQueryStore } from '@/stores/query';
  import { useBreadCrumbStore } from '@/stores/breadcrumb';

  const route = useRoute();
  const config = useRuntimeConfig();

  const queryStore = useQueryStore();
  const breadCrumbStore = useBreadCrumbStore();

  const createCanonicalLink = computed(() => {
    return config.public.NUXT_APP_DOCUMENTS.slice(0, -1);
  });

  useHead({
    title: 'Кабельторг | Купить электротехническое оборудование в Беларуси',
    meta: [{
      name: 'CabelTorg',
      content: 'Интернет магазин КабельТорг'
    }],
    link: [
      { rel: 'canonical', href: createCanonicalLink.value },
    ],
  });

  onMounted(() => {
    breadCrumbStore.changeBreadCrumb(0);
  });
</script>

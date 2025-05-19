<template>
  <div class="tools-pages">
    <div class="tools-pages__header">Показывать по: </div>
    <ul class="tools-pages__body">
      <li class="tools-pages__item" 
        v-for = "limitItem in limitItems" 
        :key = limitItem
      >
        <a href=""  
          :class="[limitItem == limit ? 'tools-pages__link active' : 'tools-pages__link']"
          @click.prevent="setLimit(limitItem)"
        >{{ limitItem }}</a>
      </li>
    </ul>
  </div>    
</template>

<script setup>
  // import { defineEmits } from 'vue';
  import { useQueryStore } from '@/stores/query';

  const router = useRouter();
  const queryStore = useQueryStore();

  const emit = defineEmits(['onLimitChanged']);

  const { limit, limitItems } = storeToRefs(queryStore);

  const setLimit = (limit) => {
    queryStore.setLimit(limit);
    const url = queryStore.createUrl();
    router.push(url);
    emit('onLimitChanged');
  };

</script>

<style scoped lang="scss">
.tools-pages {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-right: 20px;
    @media (max-width: $md3+px){
        display: none;
    }
  &__item{
    .active{
      color: #423E48;
      font-weight: 500;
    }

  }
  &__header {
    margin-right: 15px;
  }
  &__body {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-right: 20px;
  }
  a{
    font-size: 12px;
    color:#000;
    opacity: 0.8;
    transition: all ease 1ms;
    &:hover{
      color: #423E48;
      opacity: 0.8;
    }
  }

}
</style>
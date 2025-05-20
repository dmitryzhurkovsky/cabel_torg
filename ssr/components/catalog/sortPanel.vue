<template>
    <ul class="tools-sort">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <line x1="2" y1="17.1133" x2="23" y2="17.1133" stroke="#423E48" stroke-width="1.25"/>
          <line x1="23" y1="7.50391" x2="2" y2="7.5039" stroke="#423E48" stroke-width="1.25"/>
          <circle cx="16.6619" cy="16.911" r="3.08088" fill="white" stroke="#423E48" stroke-width="1.25"/>
          <circle cx="8.33806" cy="7.70623" r="3.08088" transform="rotate(-180 8.33806 7.70623)" fill="white" stroke="#423E48" stroke-width="1.25"/>
        </svg>
        <div class= "tools-sort__direction" v-if = "!sortDirection" @click.prevent="changeDirection('-')">
            <svg height="18px" width="24px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                 viewBox="0 0 512 512" xml:space="preserve">
                <path style="fill:#423E48;" d="M214.275,97.913l18.454-18.452v409.272c0,12.853,10.42,23.273,23.273,23.273
                  c12.853,0,23.273-10.42,23.273-23.273V79.459l18.454,18.452c4.544,4.544,10.501,6.817,16.455,6.817
                  c5.956,0,11.913-2.271,16.455-6.817c9.089-9.089,9.089-23.824,0-32.912L272.461,6.822c-0.543-0.543-1.116-1.058-1.711-1.547
                  c-0.267-0.219-0.548-0.41-0.821-0.614c-0.332-0.25-0.659-0.507-1.005-0.74c-0.334-0.223-0.681-0.417-1.022-0.622
                  c-0.309-0.185-0.611-0.379-0.929-0.549c-0.352-0.188-0.712-0.348-1.071-0.517c-0.329-0.155-0.653-0.32-0.991-0.461
                  c-0.351-0.144-0.709-0.262-1.064-0.389c-0.36-0.129-0.715-0.267-1.083-0.38c-0.36-0.109-0.725-0.188-1.088-0.279
                  c-0.372-0.093-0.742-0.197-1.12-0.273c-0.424-0.084-0.85-0.135-1.277-0.195c-0.326-0.047-0.645-0.109-0.974-0.141
                  c-1.53-0.15-3.07-0.15-4.6,0c-0.329,0.033-0.65,0.095-0.974,0.141c-0.427,0.061-0.853,0.11-1.277,0.195
                  c-0.38,0.076-0.748,0.18-1.12,0.273c-0.363,0.092-0.728,0.171-1.088,0.279c-0.368,0.112-0.723,0.25-1.083,0.38
                  c-0.355,0.127-0.714,0.245-1.064,0.389c-0.338,0.14-0.663,0.306-0.991,0.461c-0.358,0.169-0.72,0.329-1.072,0.517
                  c-0.318,0.171-0.619,0.365-0.929,0.549c-0.343,0.205-0.689,0.399-1.022,0.622c-0.346,0.231-0.673,0.489-1.005,0.74
                  c-0.273,0.205-0.554,0.396-0.821,0.614c-0.594,0.489-1.167,1.002-1.711,1.547l-58.178,58.179c-9.089,9.089-9.089,23.824,0,32.912
                  C190.45,107.002,205.187,107.002,214.275,97.913z"/>
            </svg>
        </div>
        <div class= "tools-sort__direction" v-if = "sortDirection"  @click.prevent="changeDirection('')">
            <svg height="18px" width="24px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                 viewBox="0 0 512.003 512.003" xml:space="preserve">
                <path style="fill:#3D6DEB;" d="M239.542,505.18c0.545,0.543,1.117,1.058,1.713,1.547c0.264,0.219,0.546,0.408,0.818,0.613
                  c0.334,0.251,0.661,0.51,1.008,0.743c0.33,0.222,0.673,0.413,1.013,0.616c0.312,0.186,0.617,0.383,0.939,0.554
                  c0.349,0.186,0.704,0.343,1.06,0.51c0.334,0.158,0.663,0.324,1.004,0.467c0.346,0.143,0.697,0.258,1.049,0.383
                  c0.366,0.132,0.728,0.272,1.1,0.385c0.352,0.105,0.706,0.185,1.061,0.273c0.382,0.098,0.76,0.203,1.15,0.281
                  c0.408,0.081,0.816,0.127,1.227,0.188c0.341,0.048,0.678,0.113,1.022,0.147c0.763,0.074,1.53,0.116,2.296,0.116
                  c0.766,0,1.533-0.04,2.296-0.116c0.346-0.034,0.681-0.099,1.022-0.147c0.411-0.059,0.819-0.107,1.227-0.188
                  c0.389-0.078,0.768-0.185,1.15-0.281c0.355-0.088,0.709-0.166,1.061-0.273c0.372-0.113,0.734-0.253,1.1-0.385
                  c0.352-0.126,0.703-0.24,1.049-0.383c0.343-0.143,0.672-0.309,1.004-0.467c0.355-0.166,0.711-0.324,1.06-0.51
                  c0.321-0.172,0.625-0.368,0.939-0.554c0.34-0.203,0.683-0.394,1.013-0.616c0.349-0.233,0.676-0.492,1.008-0.743
                  c0.273-0.205,0.554-0.394,0.818-0.613c0.596-0.487,1.168-1.002,1.713-1.547l116.359-116.361c9.089-9.089,9.089-23.824,0-32.912
                  c-9.087-9.089-23.824-9.089-32.912,0l-76.634,76.636V23.273C279.275,10.42,268.855,0,256.002,0C243.15,0,232.73,10.42,232.73,23.273
                  v409.27l-76.636-76.634c-9.087-9.089-23.824-9.089-32.912,0s-9.089,23.823,0,32.912L239.542,505.18z"/>
                </svg>
        </div>
        <li 
            :class="[item.type === sortType ? 'tools-sort__item active' : 'tools-sort__item']"
            v-for = "item in allSortsOfProduct"
            :key = "item.type"
        >
            <a href="" class="tools-sort_link" @click.prevent="changeSort(item.type)">{{ item.name }}</a>
        </li>
    </ul>
</template>

<script setup>
  // import { defineEmits } from 'vue';
  import { useQueryStore } from '@/stores/query';

  const router = useRouter();
  const queryStore = useQueryStore();

  const emit = defineEmits(['onSortChanged']);  

  const { sortType, sortDirection, allSortsOfProduct } = storeToRefs(queryStore);

  const changeSort = (type) => {
    queryStore.setSortType(type);
    const url = queryStore.createUrl();
    router.push(url);
    emit('onSortChanged');
  };

  const changeDirection = (direction) => {
    queryStore.setSortDirection(direction);
    const url = queryStore.createUrl();
    router.push(url);
    emit('onSortChanged');
  };
</script>


<style scoped lang="scss">
.tools-sort{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-right: 20px;
    @media (max-width: $md3+px){
        margin-bottom: 20px;
    }
  &__item{
    .active{
      color: #423E48;
      font-weight: 500;
    }

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
  &__direction{
    cursor: pointer;
  }
}
.active{
  color: #423E48;
  font-weight: 500;
 }

</style>
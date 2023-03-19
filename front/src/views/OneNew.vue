<template>
  <div>
    Тут страница новости
  </div>
</template>

<script>
  import axios from 'axios';
  import { mapGetters, mapMutations, mapActions } from 'vuex' 
  import CardImage from '@/components/UI/card-image.vue'

  export default {
    name: 'CardProduct',

    props: {
      id: null,
    },

    methods: {
      ...mapMutations("breadcrumb", ["ADD_BREADCRUMB", ]),
      ...mapActions("breadcrumb", ["CHANGE_BREADCRUMB", ]),
    },

    async mounted(){
      this.CHANGE_BREADCRUMB(0);
      // try {
      //     const response = await axios.get(process.env.VUE_APP_API_URL + 'products/' + this.id);
      //     this.cartItemData = response.data;
      // } catch (e) {
      //     console.log(e);
      //     this.ADD_MESSAGE({name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'})
      // }

      const mainBreadCrumb = {
        name: 'Новости',
        path: '/news',
        type: 'global',
        class: '',
      }
      this.ADD_BREADCRUMB(mainBreadCrumb);

      this.ADD_BREADCRUMB({
        name: this.$router.currentRoute.value.meta.name,
        path: this.$router.currentRoute.value.path,
        type: "global",
        class: ""
      });
    },
  }
</script>

<style lang="scss" scoped>

</style>

<template lang="html">
    <div class="header__search search-wrapper">
      <div class="search__box">
        <div class="search__field">
          <input type="text" name="focus" required class="search-box" placeholder="Поиск товаров"
                 @input="onInput"
                 v-model = "queryStringt"
          />
          <button class="icon-search" type="reset"
                  @click = "clearString"
          ></button>
        </div>

      </div>
      <div v-if ="queryStringt.length > 0" class="search__result">Ничего не найдено</div>
    </div>
</template>

<script>

export default {
  name: "HeaderSearch",

  data: function() {
    return {
        queryStringt : '',
      }
  },
  methods: {
    onInput(){
        if  (this.queryStringt.length > 0) {
          console.log('Тут запуск поиска');
        }
    },
    clearString(){
        this.queryStringt = '';
        console.log('Тут в store очищаем предыдущий поиск');
    }
  },
}
</script>

<style lang="scss" scoped>
.header{
    &__search{
      position: relative;
      // background: #FFFFFF;
      // box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
      // border-radius: 50px;
      // max-width: 384px;
      // height: 32px;
      // width: 100%;
      @media (max-width: $md2+px) {
        display: none;
      }
    }
}

//SEARCH
.search-box,.close-icon,.search-wrapper {
  position: relative;
  padding: 10px;
}
.search-wrapper {

}
.search__box {
  //width: 500px;
  background: #fff;
  height: 32px;
  display: flex;
  padding: 6px 16px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);

  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
}

.search__field{
  width: 385px;
  height: 100%;
  position: relative;

  input{
    width: 100%;
    height: 100%;
    border: 0px;
    padding-right: 38px;
    font-weight: 300;
    font-size: 14px;
    opacity: 0.5;

  }

  button{
    position: absolute;
    top: 1px;
    right: 0;
    font-size: 20px;


    cursor: pointer;
  }
}

.search__result{
  position: absolute;
  top: 40px;
  left: 10px;
  width: 96%;
  background: #fff;
  min-height: 50px;
  padding: 20px 20px;
  border-bottom-left-radius:10px;
  border-bottom-right-radius:10px;
  border-top: 2px solid rgba(0, 0, 0, 0.05) ;


}
::-webkit-input-placeholder { /* Chrome/Opera/Safari */
  color: #9fa3b1;
}
::-moz-placeholder { /* Firefox 19+ */
  color: #9fa3b1;
}
:-ms-input-placeholder { /* IE 10+ */
  color: #9fa3b1;
}



</style>

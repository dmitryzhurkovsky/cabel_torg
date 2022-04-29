<template lang="html">
    <div class="header__search search-wrapper">
      <form>
        <input type="text" name="focus" required class="search-box" placeholder="Поиск товаров" />
        <button class="close-icon" type="reset"></button>
      </form>
    </div>
</template>

<script>
export default {
}
</script>

<style lang="scss" scoped>
.header{
    &__search{
      //background: #FFFFFF;
      //box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
      //border-radius: 50px;
      //max-width: 384px;
      //height: 32px;
      //width: 100%;
    }
}

//SEARCH
.search-box,.close-icon,.search-wrapper {
  position: relative;
  padding: 10px;
}
.search-wrapper {

}
.search-box {
  background: #FFFFFF;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
  border-radius: 50px;
  max-width: 384px;
  width: 100%;
  font-size: 14px;
  opacity: 0.5;
  padding: 9px 16px;
  min-width: 300px;
}
.search-box:focus {
  border: 1px solid #bebede;
}
.close-icon {
  border:1px solid transparent;
  background-color: transparent;
  display: inline-block;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.close-icon:after {

}
.search-box:not(:valid) ~ .close-icon {
  display: none;
}


</style>

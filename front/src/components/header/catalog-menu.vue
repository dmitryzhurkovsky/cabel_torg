<template lang="html">
<!--      <div v-if = "CATALOG_ITEM_ACTIVE === 1">first category item</div>-->
<!--      <div v-if = "CATALOG_ITEM_ACTIVE === 2">second category item</div>-->
<!--      <div v-if = "CATALOG_ITEM_ACTIVE === 3">third category item</div>-->
      <div class="catalog__menu menu__container">
        <div class="menu active">
          <div class="menu__scroll">
            <div class="container row">
              <ul class="menu__mass">
                <li class="menu__item active">
                  <a class="menu__link" href="">
                    Сетевое оборудование</a>
                </li>
                <li class="menu__item ">
                  <a class="menu__link" href="">
                    Кабели и провода</a>
                </li>
                <li class="menu__item ">
                  <a class="menu__link" href="">
                    Группа 3</a>
                </li>
                <li class="menu__item">
                  <a class="menu__link" href="">
                    Группа 4</a>
                </li>
              </ul>
              <div class="menusub row">
                <div class="menusub__box">
                  <div class="menusub__item">
                    <a class="menu__rubric">Подгуппа 1</a>
                    <ul>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 1.1</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 1.2</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 1.3</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 1.4</a>
                      </li><li>
                      <a href="" class="menu__linksub">Подгруппа 1.5</a>
                    </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 1.6</a>
                      </li>
                    </ul>
                  </div>
                  <div class="menusub__item">
                    <a class="menu__rubric">Подгуппа 2</a>
                    <ul>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 2.1</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 2.2</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 2.3</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 2.4</a>
                      </li><li>
                      <a href="" class="menu__linksub">Подгруппа 2.5</a>
                    </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 2.2</a>
                      </li>
                    </ul>
                  </div>
                  <div class="menusub__item">
                    <a class="menu__rubric">Подгуппа 3</a>
                    <ul>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 3.1</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 3.2</a>
                      </li>
                    </ul>
                  </div>
                  <div class="menusub__item">
                    <a class="menu__rubric">Подгуппа 4</a>
                    <ul>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 4.1</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 4.2</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 4.3</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 4.4</a>
                      </li><li>
                      <a href="" class="menu__linksub">Подгруппа 4.5</a>
                    </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 4.6</a>
                      </li>
                    </ul>
                  </div>
                  <div class="menusub__item">
                    <a class="menu__rubric">Подгуппа 5</a>
                    <ul>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 5.1</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 5.2</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 5.3</a>
                      </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 5.4</a>
                      </li><li>
                      <a href="" class="menu__linksub">Подгруппа 5.5</a>
                    </li>
                      <li>
                        <a href="" class="menu__linksub">Подгруппа 5.6</a>
                      </li>
                    </ul>
                  </div>

                </div>

              </div>
            </div>
          </div>
        </div>
      </div>

</template>

<script>

import {mapActions, mapGetters} from 'vuex'

export default {
  name: "CatalogMenu",

  computed: {
    ...mapGetters("header", ["CATALOG_ITEM_ACTIVE"]),
  },
}
</script>

<style scoped lang="scss">
    .catalog__menu{
      position: absolute;
      top: 10px;
      left: 20px;
      padding: 38px 0;
      width: 1130px;
      height: 420px;
      background: #FFFFFF;
      box-shadow: 0px 4px 20px rgba(66, 62, 72, 0.05);
      z-index: 3;
    }
.menu{

  &__mass{
    min-width: 250px;
    max-height: 100%;
    position: static;
  }

  &__item{
    //margin: 20px 0;
    width: 100%;
    padding: 10px 0;
    &:hover{
      color:#4275D8;
      background: rgba(66, 117, 216, 0.1);
      border-radius: 6px;
      padding: 10px 0;

    }
  }




  &__link{
    font-weight: 500;
    font-size: 16px;
    line-height: 24px;
    color: #423E48;
    width: 100%;
    &:nth-child(1){
    }


  }

  .row{
    display: flex;
    align-items: flex-start;

  }

  &__rubric{
    font-weight: 400;
    font-size: 16px;
    line-height: 28px;
    text-decoration-line: underline;
    color: #423E48;

  }

  &__linksub{
    font-weight: 300;
    font-size: 14px;
    line-height: 24px;
    color: #423E48;
    &:hover{
      opacity: 0.6;
    }
  }
}

.menusub{
  display: flex;
  align-items: center;
  padding: 15px;
  box-shadow: 0px 4px 20px rgba(66, 62, 72, 0.05);
  width: 100%;
  max-height: 100%;
  position: static;
  width: 600px;

  &__box{
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
  }

  &__item{
    margin-bottom: 40px;
    margin-right: 44px;
  }



}
</style>

<template lang="html">
  <div class="burger__menu__open">
<!--    <div v-if = "MENU_ITEM_ACTIVE === 1">first menu item</div>-->
<!--    <div v-if = "MENU_ITEM_ACTIVE === 2">second menu item</div>-->
<!--    <div v-if = "MENU_ITEM_ACTIVE === 3">third menu item</div>-->
    <ul class="cd-accordion-menu animated">
      <li class="has-children">
        <input type="checkbox" name="group-1" id="group-1" checked>
        <label for="group-1">Сетевое оборудование</label>
        <ul>
          <li class="has-children">
            <input type="checkbox" name="sub-group-1" id="sub-group-1">
            <label for="sub-group-1">Маршрутизаторы</label>
            <ul>
              <li><a href="#0">Для корпоративных клиентов</a></li>
              <li><a href="#0">Для провайдеров услуг связи</a></li>
              <li><a href="#0">Аксессуары для маршрутизаторов</a></li>
            </ul>
          </li>
          <li class="has-children">
            <input type="checkbox" name="sub-group-2" id="sub-group-2">
            <label for="sub-group-2">Коммутаторы</label>
            <ul>
              <li class="has-children">
                <input type="checkbox" name="sub-group-level-3" id="sub-group-level-3">
                <label for="sub-group-level-3">Фиксированные коммутаторы</label>
                <ul>
                  <li><a href="#0">Фиксированные комутаторы</a></li>
                  <li><a href="#0">Модульные комутаторы</a></li>
                  <li><a href="#0">Коммутаторы Fibre Channel </a></li>
                  <li><a href="#0">Аксессуары для коммутаторов</a></li>
                </ul>
              </li>
              <li><a href="#0">Сервисные шлюзы</a></li>
            </ul>
          </li>
          <li><a href="#0">Сервисные шлюзы</a></li>
          <li><a href="#0">Сервисные шлюзы</a></li>
        </ul>
      </li>
      <li class="has-children">
        <input type="checkbox" name="group-2" id="group-2">
        <label for="group-2">Group 2</label>
        <ul>
          <li><a href="#0">Image</a></li>
          <li><a href="#0">Image</a></li>
        </ul>
      </li>
      <li class="has-children">
        <input type="checkbox" name="group-3" id="group-3">
        <label for="group-3">Group 3</label>
        <ul>
          <li><a href="#0">Image</a></li>
          <li><a href="#0">Image</a></li>
        </ul>
      </li>
      <li class="has-children">
        <input type="checkbox" name="group-4" id="group-4">
        <label for="group-4">Group 4</label>
        <ul>
          <li class="has-children">
            <input type="checkbox" name="sub-group-3" id="sub-group-3">
            <label for="sub-group-3">Sub Group 3</label>
            <ul>
              <li><a href="#0">Image</a></li>
              <li><a href="#0">Image</a></li>
            </ul>
          </li>
          <li><a href="#0">Image</a></li>
          <li><a href="#0">Image</a></li>
        </ul>
      </li>
    </ul>
    <div class="burger__menu__block flex-center">
      <a href="" class="burger__menu__item mb-20">Покупателям</a>
      <a href="" class="burger__menu__item">О нас </a>
    </div>
    <div class="burger__menu__block">
      <a href="tel:+375296889454" class="icon-phone burger__menu__item">+375 29 688 94 54</a>
    </div>

  </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'

export default {
  name: "BurgerMenu",

  computed: {
    ...mapGetters("header", ["MENU_ITEM_ACTIVE"]),
  },
}
</script>

<style lang="scss" scoped>

.burger__menu__open{
  position: absolute;
  top: 125px;
  width: 100%;
  height: 100%;
  background-color: #fff;
  z-index: 3;
}

a {
  text-decoration: none;
}


input {
  font-size: 1.6rem;
}


.cd-accordion-menu {
  padding: 16px 20px 16px 30px;
  border: 1px solid #F0F0F1;

}

.cd-accordion-menu ul {
  /* by default hide all sub menus */
  display: none;
  height:0px;
  transition:all 0.5s ease-in-out
}

.cd-accordion-menu li {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.cd-accordion-menu input[type=checkbox] {
  /* hide native checkbox */
  position: absolute;
  opacity: 0;
}

.cd-accordion-menu label,
.cd-accordion-menu a {
  position: relative;
  display: block;
  padding: 10px 0;
  background: #fff;
  color: #423E48;
  font-size: 12px;
  font-weight: 500;
  line-height: 12px;
}

.no-touch .cd-accordion-menu label:hover,
.no-touch .cd-accordion-menu a:hover {
  background: #52565d;
}

.cd-accordion-menu label::before,
.cd-accordion-menu label::after,
.cd-accordion-menu a::after {
  /* icons */
  content: '';
  display: inline-block;
  width: 16px;
  height: 16px;
  position: absolute;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -moz-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  -o-transform: translateY(-50%);
  transform: translateY(-50%);
}

.cd-accordion-menu label {
  cursor: pointer;
}

.cd-accordion-menu label::before,
 {
  content: "\e90e";
  font-family: icomoon;
  transform: rotate(90deg);
}

.cd-accordion-menu label::before {
  /* arrow icon */
  right: 0;
  background-position: 0 0;
  -webkit-transform: translateY(-50%) rotate(-90deg);
  -moz-transform: translateY(-50%) rotate(-90deg);
  -ms-transform: translateY(-50%) rotate(-90deg);
  -o-transform: translateY(-50%) rotate(-90deg);
  transform: translateY(-50%) rotate(-90deg);
}
.cd-accordion-menu input[type=checkbox]:checked + label::before {
  /* rotate arrow */
  -webkit-transform: translateY(-50%);
  -moz-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  -o-transform: translateY(-50%);
  transform: translateY(-50%);
}

.cd-accordion-menu input[type=checkbox]:checked + label + ul,
.cd-accordion-menu input[type=checkbox]:checked + label:nth-of-type(n) + ul {
  /* use label:nth-of-type(n) to fix a bug on safari (<= 8.0.8) with multiple adjacent-sibling selectors*/
  /* show children when item is checked */
  display: block;
  transition: all 0.3s ease-in-out;
  height:auto
}

.cd-accordion-menu ul label,
.cd-accordion-menu ul a {
  background: #fff;
  padding-left: 20px;
  color: #423E48;
}

.no-touch .cd-accordion-menu ul label:hover,
.no-touch .cd-accordion-menu ul a:hover {
  background: #3c3f45;
}

.cd-accordion-menu > li:last-of-type > label,
.cd-accordion-menu > li:last-of-type > a,
.cd-accordion-menu > li > ul > li:last-of-type label,
.cd-accordion-menu > li > ul > li:last-of-type a {
  box-shadow: none;
}

.cd-accordion-menu ul label::before {

}


.cd-accordion-menu ul ul label,
.cd-accordion-menu ul ul a {
  padding-left: 30px;
}

.cd-accordion-menu ul ul label::before {
  //left: 54px;
}


.cd-accordion-menu ul ul ul label,
.cd-accordion-menu ul ul ul a {
  padding-left: 118px;
}

.cd-accordion-menu ul ul ul label::before {
  left: 72px;
}
.burger__menu{
  color: #423E48;

  &__block{
    padding: 16px 20px 16px 30px;
    border: 1px solid #F0F0F1;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: column;
    .icon-phone{
      color: #4275D8;
      &:before{
        margin-right: 10px;
        font-size: 15px;

      }

    }
  }
  &__item{
    font-size: 12px;
    font-weight: bold;
    color:#423E48;

    a{
      color:#423E48;
      text-decoration: none;
    }

  }



  &:last-child{
    color: #4275D8;
  }


}



//@media only screen and (min-width: 600px) {
//  .cd-accordion-menu label,
//  .cd-accordion-menu a {
//    padding: 24px 24px 24px 82px;
//    font-size: 12px;
//  }
//  .cd-accordion-menu label::before {
//    left: 24px;
//  }
//  .cd-accordion-menu label::after {
//    left: 53px;
//  }
//  .cd-accordion-menu ul label,
//  .cd-accordion-menu ul a {
//    padding-left: 106px;
//  }
//  .cd-accordion-menu ul label::before {
//    left: 48px;
//  }
//  .cd-accordion-menu ul label::after,
//  .cd-accordion-menu ul a::after {
//    left: 77px;
//  }
//  .cd-accordion-menu ul ul label,
//  .cd-accordion-menu ul ul a {
//    padding-left: 130px;
//  }
//  .cd-accordion-menu ul ul label::before {
//    left: 72px;
//  }
//  .cd-accordion-menu ul ul label::after,
//  .cd-accordion-menu ul ul a::after {
//    left: 101px;
//  }
//  .cd-accordion-menu ul ul ul label,
//  .cd-accordion-menu ul ul ul a {
//    padding-left: 154px;
//  }
//  .cd-accordion-menu ul ul ul label::before {
//    left: 96px;
//  }
//  .cd-accordion-menu ul ul ul label::after,
//  .cd-accordion-menu ul ul ul a::after {
//    left: 125px;
//  }
//}
//
//.cd-accordion-menu.animated label::before {
//  /* this class is used if you're using jquery to animate the accordion */
//  -webkit-transition: -webkit-transform 0.3s;
//  -moz-transition: -moz-transform 0.3s;
//  transition: transform 0.3s;
//}



</style>

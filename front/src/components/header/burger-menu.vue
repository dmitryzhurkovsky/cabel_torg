<template lang="html">
  <div class="burger__menu__open">
    <ul class="cd-accordion-menu animated" v-if="CATALOG.length">
      <li 
        v-for   = "mainItem in CATALOG"
        :key    = "mainItem.id"
      >
        <label 
          :class = "{'active' : mainItem.mobileMenu}"  
          @click  = "changeMainCategory(mainItem, $event)"
        >
          {{ mainItem.name }}
        </label>
        <div 
            :class = "{'active' : mainItem.mobileMenu}" 
            @click  = "toggleCategory(mainItem, $event)"
            v-if="mainItem.childrens.length"
         >
              +
        </div>
        <ul class="second" v-if = "mainItem.mobileMenu && mainItem.childrens.length">
          <li 
            v-for   = "middleItem in mainItem.childrens"
            :key    = "middleItem.id"
          >
            <label 
              :class = "{'active' : middleItem.mobileMenu}"  
              @click  = "changeSubCategory(middleItem, $event)"
            >
              {{ middleItem.name }}
            </label>
            <div 
              :class = "{'active' : middleItem.mobileMenu}" 
              @click  = "toggleCategory(middleItem, $event)"
              v-if="middleItem.childrens.length"
            >
              +
            </div>
            <ul class="third" v-if = "middleItem.mobileMenu && middleItem.childrens.length">
              <li 
                class="has-children"
                v-for = "lastItem in middleItem.childrens"
                :key  = "lastItem.id"
              >
                <label for="sub-group-level-3"
                  @click = "changeLastCategory(lastItem, $event)"
                >
                  {{ lastItem.name }}
                </label>
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>

  </div>
</template>

<script>

import {mapGetters, mapMutations, mapActions} from 'vuex'

export default {
  name: "BurgerMenu",

  computed: {
    ...mapGetters("header", ["TOP_CATEGORIES_ITEM_ACTIVE", "SUB_CATEGORIES_ITEM_ACTIVE", "LAST_CATEGORIES_ITEM_ACTIVE", "CATALOG", "IS_CATALOG_OPEN"]),
  },

  methods:{
    ...mapMutations("header", ["SET_CURRENT_TOP_CATEGORY", "SET_CURRENT_SUB_CATEGORY", "SET_CURRENT_LAST_CATEGORY", "UPDATE_IS_CATALOG_OPEN"]),
    ...mapActions("catalog", ["GET_CATALOG_ITEMS"]),

    toggleCategory(item, event) {
      event.stopPropagation();
      item.mobileMenu = !item.mobileMenu;
    },
    
    changeMainCategory(category, event){
      event.stopPropagation();
      if (category.id === this.TOP_CATEGORIES_ITEM_ACTIVE) {
        this.SET_CURRENT_TOP_CATEGORY(null);
      } else {
        this.SET_CURRENT_TOP_CATEGORY(category.id);
      }
      this.openPage();
    },

    changeSubCategory(category, event){
      event.stopPropagation();
      if (category.id === this.SUB_CATEGORIES_ITEM_ACTIVE) {
        this.SET_CURRENT_SUB_CATEGORY(null);
      } else {
        this.SET_CURRENT_SUB_CATEGORY(category.id);
      }
      this.openPage();
    },

    changeLastCategory(category, event){
      event.stopPropagation();
      if (category.id === this.LAST_CATEGORIES_ITEM_ACTIVE) {
        this.SET_CURRENT_LAST_CATEGORY(null);
      } else {
        this.SET_CURRENT_LAST_CATEGORY(category.id);
      }
      this.openPage();
    },

    openPage() {
      this.UPDATE_IS_CATALOG_OPEN(!this.IS_CATALOG_OPEN);
      if (this.$router.path != '/catalog') {
          this.$router.push('/catalog');
      }
    },
  }
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
  // display: none;
  //height:0px;
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

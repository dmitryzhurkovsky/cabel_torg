<template>
    <transition-group class="popup__animation">
      <div 
        :class="[IS_POP_UP_OPEN === true ? 'popup__wrapper': 'popup__wrapper disabled']"
      >
        <div class="popup__header">
            <div class="icon-close left-menu" @click="closePopUp(false)"></div>
            <div class="right-menu">
                <TopMenuActions @click="closePopUp(false)" />
            </div>
        </div>
        <div class="popup__body">
            <div class="popoup__content">
                <div class="popup__message">Тут содежимое PopUp</div>
            </div>
        </div>
      </div>
    </transition-group>
    
</template>

<script>

  import { mapGetters, mapMutations } from "vuex";

  import TopMenuActions  from '@/components/header/header-actions.vue'

  export default {
    name: "PopUp",

    components: {
        TopMenuActions,
    },

    computed: {
        ...mapGetters("header", ["IS_POP_UP_OPEN"]),
    },

    methods: {
        ...mapMutations("header", ["SET_IS_POP_UP_OPEN"]),

        closePopUp(status) {
            console.log(this.IS_POP_UP_OPEN);
            this.SET_IS_POP_UP_OPEN(status);
            console.log(this.IS_POP_UP_OPEN);
        }
    }

  }
</script>  

<style lang="scss" scoped>
.popup {
    &__wrapper {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        // max-height:100vh;
        width: 100%;
        overflow: hidden;
        background-color: #FFFFFF;
        z-index: 95;
    }

    &__header {
        // position: absolute;
        height: 60px;
        // width: 100%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px;
        border-bottom: 1px solid #423E48 ;
    }
    &__body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }

}
.left-menu {
    cursor: pointer;
}

.disabled {
    display: none;
}
</style>

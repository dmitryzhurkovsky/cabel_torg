<template>
    <transition-group class="popup__animation">
      <div 
        :class="[IS_POP_UP_OPEN === true ? 'popup__wrapper': 'popup__wrapper disabled']"
      >



        <div class="popup__body">
            <div class="icon-close popup__close" @click="closePopUp(false)"></div>
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
        justify-content: center;
        align-items: center;
        position: absolute;
        left: 0;
        top: 0;
        //height: 100%;
        // max-height:100vh;
        width: 100%;
        background: linear-gradient(180deg, rgba(66, 62, 72, 0.2) 0%, rgba(66, 62, 72, 0) 100%);
        backdrop-filter: blur(2px);
        z-index: 95;
        height: 100vh;
        overflow-y: hidden;
    }

    &__close {
      position: absolute;
      top:0;
      right: -30px;
    }
    &__body {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 400px;
        height: 300px;
        background: #fff;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
        border-radius: 16px;

    }

}
.left-menu {
    cursor: pointer;
}

.disabled {
    display: none;
}
</style>

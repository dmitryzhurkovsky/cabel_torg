<template>
  <div>Это ХЕДЕР</div>
</template>

<script>
export default {
  name: "header"
}
</script>

<style scoped lang="scss">
.header {

    &__wrapper {

    }

    &__container {
    }

    &__body {

    }

    &__main {


    }

    &__logo {


    }
}
.menu{
    flex: 0 1 540px;
    &__body{
        @media (max-width: $md2+px) {
            position: fixed;
            width: 100%;
            //height: 100%;
            overflow: auto;
            top: -100%;
            left: 0;
            background-color: #07095E;
            transition: left 0.3s ease 0s;
            padding: 35px 15px 30px 15px;
            z-index: 2;
            &._active{
                top: 0;
            }

        }

    }
    &__list{
        margin-bottom:0;
        @media (min-width:$md2+px) {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-evenly;

        }
    }
    &__item{
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        padding: 5px 0;
        position: relative;
        // @include adaptiv-value("margin-right",35,5,1);
        margin-right: 35px;
        &:last-child{
            margin-right: 0px;
        }
        @media (max-width:$md2+px) {
            margin-bottom: 20px;
        }

    }
    &__link{
        color: $menuColor;
        // @include adaptiv-font(14, 11, 14);
        font-weight: 600;
        text-transform: uppercase;
        transition: color 0.3s ease 0s;
        &:hover{
            color: $menuColorActive;
            transition: color 300ms ease-in-out;
        }

        @media (max-width: $md2+px){
            color: #fff;
        }
    }
}


//Burger
.icon-menu {
    display: none;
    @media (max-width: $md2+px) {
        display: block;
        position: absolute;
        top: 25px;
        right: 17px;
        width: 30px;
        height: 30px;
        cursor: pointer;
        z-index: 5;
        span {
            transition: all 0.3s ease 0s;
            top: calc(50% - 1px);
            left: 0px;
            position: absolute;
            width: 100%;
            height: 3px;
            border-radius: 5%;
            background-color: #4244E7;
            &:first-child {
                top: 0px;
            }
            &:last-child {
                top: auto;
                bottom: 0px;
            }
        }
        &._active {
            span {
                transform: scale(0);
                &:first-child {
                    transform: rotate(-45deg);
                    top: calc(50% - 1px);
                }
                &:last-child {
                    transform: rotate(45deg);
                    bottom: calc(50% - 1px);
                }
            }
        }
    }
}

//==============big_header======================================================================================

//====================================================================================================


</style>

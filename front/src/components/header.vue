<template>
  <header class="header">
        <headerTop/>
        <headerBody/>
        <headerTopMenu/>
  </header>

</template>

<script>

  import HeaderBody from '@/components/header/header-body.vue'
  import HeaderTopMenu from '@/components/header/header-topmenu.vue'
  import HeaderTop from '@/components/header/header-top.vue'

  export default {
    name: "Header",

    components:
    {
      HeaderBody, HeaderTopMenu, HeaderTop
    },

  }

</script>

<style lang="scss">
.header {

    &__wrapper {
      //padding: 24px 0;
      //background: #F8FAFF;

    }

    &__container {
    }

    &__main {
    }

}

.topmenu{

  &__item{
    cursor: pointer;
  }
}

.popup-container {
  display: flex;
  justify-content: center;
  align-items: center ;
  //height: 100vh;

  .popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(#000,.5);
    z-index: 10;
    opacity: 0;
    visibility: hidden;
    transition: 400ms all;
    >label {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      cursor: pointer;
    }
    .inner {
      position: absolute;
      top: 100%;
      left: 50%;
      padding: 38px 24px 40px 24px;
      transform: translate(-50%, -50%);
      background: #fff;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);
      border-radius: 16px;
      min-width: 300px;
      box-sizing: border-box;
      transition: 400ms all;
      z-index: 10;
      max-height: 100%;
      overflow: auto;
      .close-popup{
        position: absolute;
        top: 10px;
        right: 10px;
      }
      .title {
        margin-bottom: 25px;
        position: sticky;
        top: 0;
        background: #fff;
        text-align: center;
        h6 {
          font-weight: 500;
          font-size: 20px;
          line-height: 140%;

        }
        label {
          font-size: 14px;
          color: #999;
          cursor: pointer;
          &:hover {
            color: #222;
          }
        }
      }
      .content {
        //padding: 5px 15px 15px;
        ul {
          li {
            margin-bottom: 15px;
            &:last-child {
              margin-bottom: 0;
            }
            input {
              width: 100%;
              padding: 10px 16px;
              font-size: 14px;
              box-sizing: border-box;
              background: #FFFFFF;
              border: 1px solid rgba(66, 62, 72, 0.2);
              border-radius: 8px;
              &:focus {
                outline: 0;
                border-color: #272643;
              }
            }
            button {
              background: #423E48;
              cursor: pointer;
            }
            .label_input{
              font-weight: 300;
              font-size: 12px;
              line-height: 140%;
              opacity: 0.6;
            }
          }
        }
        p {
          font-size: 13px;
          line-height: 130%;
          margin-bottom: 15px;
          &:last-child {
            margin-bottom: 0;
          }
        }
        .close-btn {
          margin-top: 15px;
          padding-top: 15px;
          border-top: 1px solid #ddd;
          label {
            background: rgba(#000, .05);
            display: block;
            line-height: 30px;
            text-align: center;
            font-size: 13px;
            color: #444;
            border-radius: 3px;
            cursor: pointer;
            &:hover {
              background: rgba(#000,.1);
            }
          }
        }
      }
    }
  }
  >input {
    position: absolute;
    left: -9999px;
    opacity: 0;
    &:checked + .popup {
      opacity: 1;
      visibility: visible;
      .inner {
        top: 50%;
      }
    }
  }
}

</style>

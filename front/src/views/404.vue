<template>
  <div class="structure">
    <div class="structure__wrapper">
      <div class="structure__content _container">
        <div class="structure__body">
        </div>
        <div class="structure__block">
          <h3 class="structure__title">Что-то пошло не так...</h3>
          <div class="structure__text">Так уж получилось, что из множества страниц нашего сайта Вы оказались как раз на той, которая уже не существует…</div>
          <button class="btn">Вернуться на главную</button>

      </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: '404',
  }
</script>

<style scoped lang="scss">

.structure {

  &__wrapper{



  }
  &__content{

  }

  &__body{
    background-image: url("../assets/404.png");
    background-position: top center;
    background-repeat: no-repeat;
    min-height: 500px;

  }
  &__title{
    margin-bottom: 30px;


  }
  &__text{
    width: 50%;
    margin: 0 auto;
  }
  &__block{
    text-align: center;
    padding: 20px 0 60px 0;
    button{
      background: #423E48;
      margin-top: 30px;
    }


  }
  &__item{

  }


}


</style>

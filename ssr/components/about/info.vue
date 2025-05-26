<template>
  <div class="about">
    <div class="about__wrapper">
      <div class="about__content _container">
        <div class="about__body">
            <div class="about__section_title section_title">О компании</div>
            <div>
              <p>Компания ООО «КабельЭлектроТорг» с 2011 осуществляет поставку высококачественной кабельных изделий и
                сетевого оборудования на белорусский рынок. Если вы ищете, где купить кабель или провода в Минске, то добро пожаловать!</p>
              <p>За более чем 10 лет работы мы зарекомендовали себя как надёжный поставщик электротехнической продукции,
                в первую очередь ориентированный на клиента. Ставку в своей работе мы делаем на усиление позиций в
                белорусском регионе и расширении географии продаж по стране в целом.  <a class="_link" href="/about">Подробнее...</a></p>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped lang="scss">

.about {

  &__wrapper{
    padding: 20px 0;

  }
  &__body{
    background: #FFFFFF;
    border: 2px solid #EEEEEE;
    box-sizing: border-box;
    border-radius: 8px;
    padding: 28px 28px;
    p{
      font-size: 14px;
      line-height: 130%;
      color: #423E48;
      opacity: 0.8;
      &:nth-child(1){
        margin: 10px 0 20px 0;
      }
    }
  }
}

</style>
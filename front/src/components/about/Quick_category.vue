<template>
  <div class="quick-category">
    <div class="quick-category__wrapper">
      <div class="quick-category__content _container">
        <div class="quick-category__body">
          <h3>Каталог товаров</h3>
          <div class="quick-category__grid">
            <div class="quick-category__item quick-category__big">
            <!-- <div class="quick-category__item quick-category__big" :style = "{backgroundImage : 'url(' + getPath('cat1.png') + ')'}"> -->
              <ul class="quick-category__list">Сетевое оборудование
                <li class="quick-category__link">
                  <a href="">Коммутаторы </a> </li>
                <li class="quick-category__link"><a href="">Маршрутизаторы</a></li>
                <li class="quick-category__link"><a href="">Медиаконвекторы</a></li>
                <li class="quick-category__link"><a href="">Сервисные шлюзы</a></li>
                <li class="quick-category__link"><a href="">Сетевые ПО</a></li>
              </ul>
              <a href="" class="quick-category__more">Смотреть все <span>&#8594;</span></a>
            </div>
            <div class="quick-category__item quick-category__big-row">
              <div class="quick-category__list">Кабели и провода</div>
              <a href="" class="quick-category__more">Смотреть все <span>&#8594;</span></a>
            </div>
            <div class="quick-category__item">
              <div class="quick-category__list">Оптическое оборудование</div>
              <a href="" class="quick-category__more">Смотреть все <span>&#8594;</span></a>
            </div>
            <div class="quick-category__item">
              <div class="quick-category__list">Оборудование для ТВ</div>
              <a href="" class="quick-category__more">Смотреть все <span>&#8594;</span></a>

            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'Quick_category',

    methods: {
      getPath: function(item){
        console.log(process.env.BASE_URL);
        console.log(process.env.VUE_APP_IMAGES);
        let path = process.env.VUE_APP_IMAGES + item;
        // return path;
        return item;
      },

    }
  }
</script>

<style scoped lang="scss">

h3{
  margin-bottom: 20px;
}

@media (min-width: $md2+px){
  .quick-category__grid{
    display: grid;
    gap:10px;
    grid-template: minmax(180px, 1fr) minmax(180px, 1fr) / 2fr 1fr 1fr ;
  }
}

@media (max-width: $md3+px){
  .quick-category__grid {
    display: flex;
    flex-direction: column;
    gap: 15px;

  }
}

.quick-category__item{

  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 21px 24px;
  border: 2px solid #EEEEEE;
  border-radius: 8px;
  background: #fff;
  background-position: right;
  background-repeat: no-repeat;


  &:nth-child(2){
    background-image: url("../../assets/category/cat2.png");
    background-size: contain;
  }
  &:nth-child(3){
    background-image: url("../../assets/category/cat3.png");
  }
  &:nth-child(4){
    background-image: url("../../assets/category/cat4.png");
  }

}
.quick-category__big{
  grid-row: span 2;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-image: url("../../assets/category/cat1.png");
  background-position: right;
  background-repeat: no-repeat;
  @media (max-width: $md3+px){
    background-size: contain;
  }

}
.quick-category__big-row{
  grid-column: span 2;

}
.quick-category__list{
  font-weight: 500;
  font-size: 20px;
  line-height: 24px;
  color: #423E48;
  @media (max-width: $md3+px) {
    max-width: 120px;

  }
}
.quick-category__link{
  list-style: none;
  //&:hover{
  //  font-weight: 500;
  //  color:#000
  //}
  &:nth-child(1){
    margin-top: 20px;
  }
}

.quick-category__link a{
  text-decoration:none;
  font-weight: 400;
  font-size: 14px;
  line-height: 2;
  color: #423E48;
  opacity: 0.4;
  &:hover{
    color: #423E48;
    opacity: 1;
  }
}




.quick-category__more {
  font-weight: 400;
  font-size: 14px;
  line-height: 130%;
  color: #4275D8;
  @media (max-width: $md3+px) {
    display: none;
  }
}
</style>

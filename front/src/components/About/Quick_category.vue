<template>
  <div class="quick-category">
    <div class="quick-category__wrapper">
      <div class="quick-category__content _container">
        <div class="quick-category__body">
            <h3>Каталог товаров</h3>
            <div class="quick-category__main_block flex-center">
             <div class="table2x flex-center">
               <ul class="quick-category__list">Сетевое оборудование
                   <li class="quick-category__item">
                     <a href="">Коммутаторы</a> </li>
                   <li class="quick-category__item"><a href="">Маршрутизаторы</a></li>
                   <li class="quick-category__item"><a href="">Медиаконвекторы</a></li>
                   <li class="quick-category__item"><a href="">Сервисные шлюзы</a></li>
                   <li class="quick-category__item"><a href="">Сетевые ПО</a></li>
                 </ul>
                 <a href="" class="quick-category__link">Смотреть все <span>&#8594;</span></a>
             </div>


             <div class="table2x flex-center">
               <div class="table2x__row">
                 <div class="quick-category__list">Кабели и провода</div>
                 <a href="" class="quick-category__link">Смотреть все <span>&#8594;</span></a>
               </div>
               <div class="table2x__row flex-center">
                 <div class="table2x">
                   <div class="quick-category__list">Оптическое оборудование</div>
                   <a href="" class="quick-category__link">Смотреть все <span>&#8594;</span></a>
                 </div>
                 <div class="table2x">
                   <div class="quick-category__list">Оборудование для ТВ</div>
                   <a href="" class="quick-category__link">Смотреть все <span>&#8594;</span></a>

                 </div>
               </div>

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
  }
</script>

<style scoped lang="scss">

.quick-category {

  &__wrapper{
    padding: 20px 0;

  }
  &__content{

  }

  &__body{
    .table2x{

      width: 100%;
      &:nth-child(1){
        padding: 28px 24px;
        margin: 0 10px 0 0;
        align-items: flex-start;
        flex-basis: 50%;
        flex-direction: column;
        border: 2px solid #EEEEEE;
        box-sizing: border-box;
        border-radius: 8px;
        background: linear-gradient(180deg, rgba(246, 247, 249, 0) 0%, #F6F7F9 50.31%, rgba(246, 247, 249, 0) 100%);
        &:hover{
          border: 2px solid #4275D8;
          box-sizing: border-box;
          border-radius: 8px;
        }
      }

      &:nth-child(2){
        flex-basis: 50%;
        flex-direction: column;
        margin: 0 0 0 10px;
        .table2x__row{
          &:nth-child(1){
            width: 100%;
            padding: 28px 24px;
            border: 2px solid #EEEEEE;
            box-sizing: border-box;
            border-radius: 8px;
            background: linear-gradient(180deg, rgba(246, 247, 249, 0) 0%, #F6F7F9 50.31%, rgba(246, 247, 249, 0) 100%);
            &:hover{
              border: 2px solid #4275D8;
              box-sizing: border-box;
              border-radius: 8px;
            }
          }
          &:nth-child(2){
            padding: 20px 0 0 0;
            .table2x{
              padding: 28px 24px;
              border: 2px solid #EEEEEE;
              box-sizing: border-box;
              border-radius: 8px;
              background: linear-gradient(180deg, rgba(246, 247, 249, 0) 0%, #F6F7F9 50.31%, rgba(246, 247, 249, 0) 100%);
              &:hover{
                border: 2px solid #4275D8;
                box-sizing: border-box;
                border-radius: 8px;
              }
              &:nth-child(1){
              }
            }

          }
        }

      }

    }

      }

  &__main_block{
    width: 100%;

  }
  &__list{
    font-weight: 500;
    font-size: 20px;
    line-height: 24px;
    color: $mainColor;

  }

  &__item{
    a{
      font-weight: 400;
      font-size: 14px;
      line-height: 130%;
      color: #423E48;
      opacity: 0.4;
      &:hover{
        color: $mainColor;
      }
    }

  }
  &__link{
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
    color: #4275D8;
  }


}

.table_box_style{
  padding: 28px 24px;
  border: 2px solid #EEEEEE;
  box-sizing: border-box;
  border-radius: 8px;
  background: linear-gradient(180deg, rgba(246, 247, 249, 0) 0%, #F6F7F9 50.31%, rgba(246, 247, 249, 0) 100%);
  &:hover{
    border: 2px solid #4275D8;
    box-sizing: border-box;
    border-radius: 8px;
  }

}

</style>
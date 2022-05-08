<template>
  <div class="catalog">
    <div class="catalog__wrapper">
      <div class="catalog__content _container">
        <div class="catalog__body">

          <ul class="breadcrumb">
            <li><a href="#">Главная</a></li>
            <li class="breadcrumb__separater icon-arrow-l"></li>
            <li><a href="#">Каталог</a></li>
            <li class="breadcrumb__separater icon-arrow-l"></li>
            <li><a href="#">Подраздел каталога</a></li>

          </ul>
          <div class="catalog__block">

<!--        # SIDEBAR-->
            <div class="catalog__sidebar filter">
              <div class="filter__block">
                <div class="filter__box">
                  <div class="filter__title icon-arrow-l">Тип оборудования</div>

                  <div class="filter__checkbox-list">
                    <div class="filter__checkbox__item">
                      <div class="checkbox-default">
                        <label class="checkbox__label">
                          <input type="checkbox" name="" class="" value="">
                          <div class="checkbox"></div>
                          <div class="">
                            <span class="jsx-1900692967">Кабели и провода</span>
                          </div>
                        </label>
                      </div>
                    </div>
                    <div class="filter__checkbox__item">
                      <div class="checkbox-default">
                        <label class="checkbox__label">
                          <input type="checkbox" name="" class="" value="">
                          <div class="checkbox"></div>
                          <div class="">
                            <span class="jsx-1900692967">Сетевое оборудование</span>
                          </div>
                        </label>
                      </div>
                    </div>
                    <div class="filter__checkbox__item">
                      <div class="checkbox-default">
                        <label class="checkbox__label">
                          <input type="checkbox" name="" class="" value="">
                          <div class="checkbox"></div>
                          <div class="">
                            <span class="jsx-1900692967">Группа 3</span>
                          </div>
                        </label>
                      </div>
                    </div>
                  </div>


                </div>
                <div class="filter__box">
                  <div class="filter__title icon-arrow-l">Категория</div>

                  <div class="filter__checkbox-list">
                    <div class="filter__checkbox__item">
                      <div class="checkbox-default">
                        <label class="checkbox__label">
                          <input type="checkbox" name="" class="" value="">
                          <div class="checkbox"></div>
                          <div class="">
                            <span class="jsx-1900692967">Плинты размыкаетмые</span>
                          </div>
                        </label>
                      </div>
                    </div>
                    <div class="filter__checkbox__item">
                      <div class="checkbox-default">
                        <label class="checkbox__label">
                          <input type="checkbox" name="" class="" value="">
                          <div class="checkbox"></div>
                          <div class="">
                            <span class="jsx-1900692967">Коннекторы, разъемы, соединители</span>
                          </div>
                        </label>
                      </div>
                    </div>
                    <div class="filter__checkbox__item">
                      <div class="checkbox-default">
                        <label class="checkbox__label">
                          <input type="checkbox" name="" class="" value="">
                          <div class="checkbox"></div>
                          <div class="">
                            <span class="jsx-1900692967">Категория 3</span>
                          </div>
                        </label>
                      </div>
                    </div>
                  </div>


                </div>
                <div class="filter__box">
                  <div class="filter__title icon-arrow-l">Показывать:</div>

                  <div class="filter__checkbox-list">
                    <div class="filter__checkbox__item">
                      <div class="checkbox-default">
                        <label class="checkbox__label">
                          <input type="checkbox" name="" class="" value="">
                          <div class="checkbox"></div>
                          <div class="">
                            <span class="jsx-1900692967">Все товары</span>
                          </div>
                        </label>
                      </div>
                    </div>
                    <div class="filter__checkbox__item">
                      <div class="checkbox-default">
                        <label class="checkbox__label">
                          <input type="checkbox" name="" class="" value="">
                          <div class="checkbox"></div>
                          <div class="">
                            <span class="jsx-1900692967">Только товары со скидкой</span>
                          </div>
                        </label>
                      </div>
                    </div>
                    <div class="filter__checkbox__item">
                      <div class="checkbox-default">
                        <label class="checkbox__label">
                          <input type="checkbox" name="" class="" value="">
                          <div class="checkbox"></div>
                          <div class="">
                            <span class="jsx-1900692967">Только “В наличии”</span>
                          </div>
                        </label>
                      </div>
                    </div>
                  </div>


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
    name: 'Catalog',
  }
</script>

<style scoped lang="scss">

.catalog {

  &__wrapper{

  }
  &__content{

  }

  &__body{
  }


  &__item{

  }
  &__block{

}
  &__sidebar{
    width: 270px;
  }


}

.filter{

  &__block{

  }
  &__checkbox{

    &__item{
      margin: 0px 15px 10px 0px;
      height: 18px;
      input{
        position: absolute;
        opacity: 0;
        z-index: -1;
      }
    }


  }
  &__box{
    font-weight: 400;
    position: relative;

  }

  &__title{
    background: #F8FAFF;
    padding: 6px 8px;
    font-weight: 500;
    font-size: 14px;
    line-height: 24px;
    color: #423E48;
    margin: 12px 0;
    &:before{
      position: absolute;
      right: 10px;
      transform: rotate(-90deg);
    }
  }

}
.checkbox{
  margin-right: 12px;



  &:before{
    content: "";
    width: 18px;
    height: 18px;
    display: inline-block;
    background: rgb(249, 249, 249);
    border: 1px solid rgb(163, 163, 163);
  }


  &__label{
    display: flex;
    align-items: center;
    justify-content: flex-start;
    height: 30px;
  }
}

</style>
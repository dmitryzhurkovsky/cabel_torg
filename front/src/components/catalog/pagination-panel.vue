<template>
    <div class="content-block__pagination">
        <a class="pagination_link active">1</a>
        <a class="pagination_link">2</a>
        <a class="pagination_link">3</a>
        <a class="pagination_link">...</a>
        <a class="pagination_link">5</a>
        <a class="pagination_link">6</a>
    </div>   
</template>

<script>

  import {mapGetters} from 'vuex'

  export default {
    name: 'PaginationPanel',
  }
</script>

<style scoped lang="scss">
.pagination_link{
    width: 40px;
    height: 40px;
    background: rgba(66, 62, 72, 0.07);
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #423E48;
    transition: all 0.3s ease;
    &:hover{
      border: 1.2px solid #4275D8;
      cursor: pointer;
    }
  }
  .active{
    background: #4275D8;
    color: #fff;
  }
</style>
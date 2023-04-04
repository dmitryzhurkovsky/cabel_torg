<script setup lang="ts">
  import { computed, PropType, ref, watch } from 'vue';
  import { ITableHeadItem } from '../../types'
  import TableRow from '@/components/Table/TableRow.vue'
  import TableColumn from '@/components/Table/TableColumn.vue'
  import Button from '@/components/UI/Button.vue'
  import Select from '@/components/UI/Select.vue'

  const props = defineProps({
    tableData: {
      type: Object as PropType<Array<any>>,
      required: true
    },
    columnTemplates: {
      type: String,
      required: true
    },
    head: {
      type: Object as PropType<Array<ITableHeadItem>>,
      required: true
    },
    uploadButton: {
      type: Boolean,
      required: false,
      default: false
    },
    addButton: {
      type: Boolean,
      required: false,
      default: true
    },
    editButton: {
      type: Boolean,
      required: false,
      default: true
    },
    deleteButton: {
      type: Boolean,
      required: false,
      default: true
    },
  })
  const emit = defineEmits<{
    (event: 'editRow', id: string): void
    (event: 'uploadRow', id: string): void
    (event: 'deleteRow', id: string): void
    (event:'openForm'): void
  }>()

  const sortField = ref('id')
  const typeSort = ref('desc')
  const itemsInPage = ref(20)
  const pageNumber = ref(1)
  const totalPages = ref(1)

  const itemsInPageArray = [
    {id: 10, name: '10'},
    {id: 20, name: '20'},
    {id: 50, name: '50'},
  ]

  const tableDataSorting = computed(() => {
    return props.tableData.sort((a, b) => {
      let modifier = 1;
      if (typeSort.value === 'desc') modifier = -1
      const param = sortField.value;
      let sortAs = 'string'
      if (typeof a[param] === 'number') {
        sortAs = 'number'
      }
      if (typeof a[param] === 'string' && param === 'id') {
        if (a[param].indexOf('Заказ # ') !== -1) {
          sortAs = 'id'
        } else {
          sortAs = 'string'
        }
      }
      if (sortAs === 'string') {
        if (Number(a[param]) < Number(b[param])) return -1 * modifier
        if (Number(a[param]) > Number(b[param])) return 1 * modifier
        return 0
      } else if (sortAs === 'id') {
        const aModified = a[param].slice(8)
        const bModified = b[param].slice(8)
        if (Number(aModified) < Number(bModified)) return -1 * modifier
        if (Number(aModified) > Number(bModified)) return 1 * modifier
        return 0
      } else{
        if (a[param] < b[param]) return -1 * modifier
        if (a[param] > b[param]) return 1 * modifier
        return 0
      } 
    })
  })

  const tableDataPaginating = computed(() => {
    let start = (pageNumber.value - 1) * itemsInPage.value
    if (start > tableDataSorting.value.length) {
      totalPages.value = Math.ceil(tableDataSorting.value.length / itemsInPage.value);
      pageNumber.value = totalPages.value
      start = (totalPages.value - 1) * itemsInPage.value
    }
    return tableDataSorting.value.slice(start, start + itemsInPage.value)
  })

  const sortFieldName = computed(() => {
    return props.head.filter(item => item.db === sortField.value)[0].name
  })

  const typeSortName = computed(() => {
    return typeSort.value === 'asc' ? 'А-Я' : 'Я-А'
  })

  const setSort = (name: string) => {
    if (sortField.value === name) {
      if (typeSort.value === 'asc') {
        typeSort.value = 'desc'
      } else {
        typeSort.value = 'asc'
      }
    } else {
      sortField.value = name
    }
  }

  const onChangePageNumber = (page: number) => {
    if (pageNumber.value !== page && page !== 0) {
      if (page > 0 && page < totalPages.value + 1) {
        pageNumber.value = page
      }
    }
  }

  const onChangeItemsInPage = (value: number) => {
    itemsInPage.value = value
    totalPages.value = Math.ceil(props.tableData.length / itemsInPage.value);
  }

  const onAddButtonClick = () => {
    emit('openForm')
  }

  const onEditButtonClick = (id: string) => {
    emit('editRow', id)
  }

  const onUploadButtonClick = (id: string) => {
    emit('uploadRow', id)
  }

  const onDeleteButtonClick = (id: string) => {
    emit('deleteRow', id)
  }

  watch(() => props.tableData,
    () => {
      onChangeItemsInPage(itemsInPage.value)
  });

  // onBeforeUpdate(() => {
  //   onChangeItemsInPage(itemsInPage.value)
  // })

</script>
<template>
  <div class="table-infowrapper" v-if="tableDataPaginating">
    <div class="table-info info">
      <span class="info-elem">Сортировка по полю: {{sortFieldName}}</span>
      <span class="info-elem">Сортируем по направлению: {{typeSortName}}</span>
      <Button v-if="addButton" label="Добавить" @click="onAddButtonClick()"></Button>
    </div>

    <div class="table-pagination">
        <!-- <div 
            :class="[pageNumber > 1 ? 'pagination-item active' : 'pagination-item']"
            @click="onChangePageNumber(1)"
        >{{ '<<' }}</div> -->
        <div
            :class="[pageNumber > 1 ? 'pagination-item active' : 'pagination-item']"
            @click="onChangePageNumber(pageNumber - 1)"
        >{{ '<' }}</div>
        <div class="pagination-pages news__pagenumber">{{ pageNumber }} / {{ totalPages }}</div>
        <!-- <span>{{ '/' }}</span>
        <div class="pagination-item news__pagenumber">{{ totalPages }}</div> -->
        <div 
            :class="[pageNumber < totalPages ? 'pagination-item active' : 'pagination-item']"
            @click="onChangePageNumber(pageNumber + 1)"
        >{{ '>' }}</div>
        <!-- <div 
            :class="[pageNumber < totalPages ? 'pagination-item active' : 'pagination-item']"
            @click="onChangePageNumber(totalPages)"
        >{{ '>>' }}</div> -->
        <div class="pagination-selector">
          <Select
            :text = String(itemsInPage)
            :id   = String(itemsInPage)
            fieldForSearch = "name"
            :data = "itemsInPageArray"
            @onSelectItem="onChangeItemsInPage"
          />
        </div>
    </div>
  </div>

  <div class="table-wrapper">
    <div class="table">
      <div
        class="table-head"
        :style="{'grid-template-columns': columnTemplates}">
        <div
          class="table-head__name"
          v-for="(element) of props.head"
          :key="element.db"
          @click="setSort(element.db)">
          {{element.name}}
        </div>
      </div>
      <table-row
        v-for="rowData in tableDataPaginating"
        :key="rowData.id"
        :columnTemplates="columnTemplates"
      >
        <table-column 
          v-for="(col) of props.head"
          :image="col.type === 'image'"
          :srcImage="rowData[col.src]"
          :vHtml="col.type === 'v-html'"
          :key="col.db"
          :columnTitle="col">
          {{rowData[col.db]}}
        </table-column>
        
        <table-column 
          v-if="uploadButton"
          :columnTitle="{db: 'Upload', name: ''}"
        >
          <Button icon="file" @click="onUploadButtonClick(rowData)"></Button>
        </table-column>
        <table-column 
          v-if="editButton"
          :columnTitle="{db: 'Edit', name: ''}"
        >
          <Button icon="pen-to-square" @click="onEditButtonClick(rowData)"></Button>
        </table-column>
        <table-column
          v-if="deleteButton"
          :columnTitle="{db: 'Del', name: ''}"
        >
          <Button icon="trash-can" color="danger" @click="onDeleteButtonClick(rowData)"></Button>
        </table-column>
      </table-row>
    </div>
  </div>

  <div class="table-pagination">
      <!-- <div 
          :class="[pageNumber > 1 ? 'pagination-item active' : 'pagination-item']"
          @click="onChangePageNumber(1)"
      >{{ '<<' }}</div> -->
      <div
          :class="[pageNumber > 1 ? 'pagination-item active' : 'pagination-item']"
          @click="onChangePageNumber(pageNumber - 1)"
      >{{ '<' }}</div>
      <div class="pagination-item news__pagenumber">{{ pageNumber }}</div>
      <span>{{ '/' }}</span>
      <div class="pagination-item news__pagenumber">{{ totalPages }}</div>
      <div 
          :class="[pageNumber < totalPages ? 'pagination-item active' : 'pagination-item']"
          @click="onChangePageNumber(pageNumber + 1)"
      >{{ '>' }}</div>
      <!-- <div 
          :class="[pageNumber < totalPages ? 'pagination-item active' : 'pagination-item']"
          @click="onChangePageNumber(totalPages)"
      >{{ '>>' }}</div> -->
      <div class="pagination-selector">
        <Select
          :text = String(itemsInPage)
          :id   = String(itemsInPage)
          fieldForSearch = "name"
          :data = "itemsInPageArray"
          @onSelectItem="onChangeItemsInPage"
        />
      </div>
  </div>

</template>

<style lang="scss" scoped>
.table {
  background-color: #fff;
  width: 100%;
  margin-bottom: 40px;
  margin-top: 15px;
  &-pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 20px 0;
  }
  &-wrapper {
    display: flex;
    justify-content: center;
  }
  &-infowrapper {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  &-head {
    padding: 5px 16px;
    display: grid;
    column-gap: 10px;
    align-items: center;
    border-bottom: 2px solid #EEEFF4;
    background: #fff;
    &__name {
      display: flex;
      justify-content: flex-start;
      align-items: center;
      color: #999;
      cursor: pointer;
    }
    @media screen and (max-width: 767px) {
      display: none;
    }
  }
}
.info{
  display: flex;
  justify-content: flex-start;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  &-elem{
    display: inline-block;
    padding: 10px;
    border: 1px solid var(--primary);
  }
  &-elem:first-child{
    border-top-left-radius: 7px;
    border-bottom-left-radius: 7px;
    border-right: none;
  }
  &-elem:nth-child(2) {
    border-top-right-radius: 7px;
    border-bottom-right-radius: 7px;
  }
  &-button{
    margin: auto 0;
    margin-left: auto;
  
    display: inline-block;
  }
}

.pagination{
  &-selector{
    max-width: 100px;
  }
  &-pages{
    border: 1px solid var(--primary);
    padding: 10px 10px;
    height: 40px;
    border-radius: 7px;
    font-size: 15px;
    width: 100%;
    text-align: center;
  }
  &-item{
    border: 1px solid var(--primary);
    padding: 10px 10px;
    height: 40px;
    border-radius: 7px;
    font-size: 15px;
    width: 40px;
    text-align: center;
  }
}

.active {
  cursor: pointer;
  &:hover{
    background-color: var(--primary-hover);
    color: var(--background-content);
  }

}
</style>
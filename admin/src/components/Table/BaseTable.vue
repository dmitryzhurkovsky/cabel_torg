<script setup lang="ts">
  import { computed, PropType, ref } from 'vue';
  import { ITableHeadItem } from '../../types'
  import TableRow from '@/components/Table/TableRow.vue'
  import TableColumn from '@/components/Table/TableColumn.vue'
  import Button from '@/components/UI/Button.vue'
  import { watch } from 'fs';

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
  const typeSort = ref('asc')

  const tableDataSorting = computed(() => {
    return props.tableData.sort((a, b) => {
      let modifier = 1;
      if (typeSort.value === 'desc') modifier = -1
      const param = sortField.value;
      if (a[param] < b[param]) return -1 * modifier
      if (a[param] > b[param]) return 1 * modifier
      return 0
    })
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

</script>
<template>
  <div class="table-info info">
    <span class="info-elem">Сортировка по полю: {{sortField}}</span>
    <span class="info-elem">Сортируем по направлению: {{typeSort}}</span>
    <Button v-if="addButton" label="Добавить" @click="onAddButtonClick()"></Button>
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
        v-for="rowData in tableDataSorting"
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
</template>

<style lang="scss" scoped>
.table {
  background-color: #fff;
  width: 100%;
  margin-bottom: 40px;
  margin-top: 15px;
  &-wrapper {
    display: flex;
    justify-content: center;
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

</style>
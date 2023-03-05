<template>
  <div :class="[isDropDownOpen ? 'selector-content selector-content__open' : 'selector-content']">
    <div class="selector-filer">
      <input class="InputChevron input"
        :class="[activeItem ? 'choosen' : 'notchoosen']"
        v-if="data"
        v-model = "searchField"
        type="text"
        @click="onToggleDropDown()"
        @keyup="onKeyPress"
        @input="onInput"
      />
      <Icon  v-if="!isDropDownOpen"
        icon = "square-caret-down"
        color="primary" 
        @click="onToggleDropDown()"
      />
      <Icon v-if="isDropDownOpen"
        icon = "square-caret-up"
        color="primary" 
      />
    </div>
    <ul v-if="data&&isDropDownOpen" class='dropdown-menu'>
      <li class="dropdown-item"
        v-for="item in filteredItems"
        :key="item.id"
        :id="item.id"
        @click="onSelectItem(item)"
      >{{item[props.fieldForSearch]}}</li>
    </ul>
  </div>
</template>

<script setup lang="ts">

import Icon from '@/components/UI/Icon.vue'
import { computed, onBeforeUnmount, onMounted, PropType, ref } from "vue";
import { IDeliveryType} from "../../types";

  const props = defineProps({
    text: {
      type: String,
      required: false,
      default: '',
    },
    id: {
      type: String,
      required: true,
      default: ''
    },
    data: {
      type: Object as PropType<Array<IDeliveryType>>,
      required: false,
      default: []
    },
    fieldForSearch: {
      type: String,
      requered: true,
      default: 'name'
    },
    limit: {
      type: Number, 
      required: false,
      default : 10
    },
  })

  const emit = defineEmits<{
    (event: 'onSelectItem', item: string): void

  }>()

  const isDropDownOpen = ref(false)
  const searchField = ref(props.text)
  const activeItem = ref(props.id)
  const isSelectorActive = ref(false)
  const PrevValue = ref(props.text)

  const filteredItems = computed(() => {
    let InputText = searchField.value;
    let NotLimit = props.data.filter((elem) =>
    {
        if(InputText==='') return true
        const name = elem[props.fieldForSearch].toLowerCase() as string
        return name.indexOf(InputText.toLowerCase()) > -1
    });

    NotLimit.sort(function(a, b){
      let x = a[props.fieldForSearch] as string
      let y = b[props.fieldForSearch] as string
      return x.toLowerCase() < y.toLowerCase() ? -1 : x.toLowerCase() > y.toLowerCase() ? 1 : 0
    });

    let Iteration = props.limit
    let Limit = []
    if (NotLimit.length < Iteration) Iteration = NotLimit.length
    for (let i = 0; i < Iteration; i++){
        Limit[i] = NotLimit[i]
    }
    return Limit
  })

  const onSelectItem = (elem: IDeliveryType) =>{
    activeItem.value = elem.id as string
    searchField.value = elem[props.fieldForSearch] as string
    isDropDownOpen.value = false
    isSelectorActive.value = false
    emit('onSelectItem', activeItem.value)
  }

  const onToggleDropDown = () =>{
    isDropDownOpen.value = true
    PrevValue.value = searchField.value
    searchField.value  = ""
    isSelectorActive.value = true
  }

  const onInput = () => {
    if (!isSelectorActive.value) {
      isDropDownOpen.value = true
      PrevValue.value = searchField.value
      isSelectorActive.value = true
    }
  }

  const HideSelect = () => {
    if (isSelectorActive.value){
      isDropDownOpen.value = false
      isSelectorActive.value = false
      searchField.value = PrevValue.value
    }
  }

  const onKeyPress = (event: KeyboardEvent) => {
    if (event.keyCode === 13) {
      // console.log(event.keyCode)
      activeItem.value = filteredItems.value[0].id as string
      searchField.value = filteredItems.value[0][props.fieldForSearch] as string
      isDropDownOpen.value = false
      isSelectorActive.value = false
      emit('onSelectItem', activeItem.value)
    }
  }

  onMounted(() => {
    document.addEventListener('click', HideSelect.bind(this), true)
    searchField.value   = props.text
    activeItem.value    = props.id
    isSelectorActive.value  = false
    isDropDownOpen.value    = false
  })

  onBeforeUnmount(() => {
      document.removeEventListener('click', HideSelect.bind(this), true)
  })

</script>

<style lang="scss" scoped>
  .selector{
    &-content{
      position: relative;
      background: var(--background-content);
      border: 1px solid var(--primary);
      border-radius: 6px;
      &:enabled:hover {
        background: var(--primary-hover);
      }
      &__open{
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 0;
      }
    }  
    &-filer{
      display: flex;
      justify-content: space-between;
      position: relative;
      align-items: center;
      cursor: pointer;
      width: 100%;
      input{
        width: 100%;
        color:#9595A0
      }
    }
  }
  .dropdown {
    &-menu{
      position: absolute;
      margin-left: -1px;
      z-index: 20;
      top: 40px;
      left: 0;
      width: calc(100% + 2px);
      border-radius: 0 0 6px 6px;
      border: 1px solid var(--primary);
      background-color: var(--background-content);
    }
    &-item {
      display: block;
      width: 100%;
      padding: 0.4rem 1rem;
      clear: both;
      text-align: inherit;
      background-color: transparent;
      border: 0;
      height: 40px;
      &:hover{
        color:var(--primary-hover);
      }
    }
  }

  ul {
    position: relative;
    list-style: none;
    padding: 0;
    margin: 0;
  }
  li {
    cursor: pointer;
  }
  input {
    background-color: transparent;
    border: none;
    outline: none;
  }
</style>

<script setup lang='ts'>
import { ref, watch, onMounted, onBeforeUnmount } from "vue";
import { useStore } from '../../store';
import { MutationTypes } from '../../store/mutation-types'
import { ActionTypes } from '../../store/action-types';
import { router } from '../../router'

const props = defineProps({
  openSidebar: {
    type: Boolean,
    required: true,
  },
})

const store = useStore()
const intervalID = ref()
const isFailedParsing = ref(false)
const lastParsingStarted = ref('')
const lastParsingFinished = ref('')
const emit = defineEmits(['onToggleMenu']);

watch(() => store.getters.parserStatus,
  (curr, prev) => {
      isFailedParsing.value = curr.is_failed
      lastParsingStarted.value = new Date(curr.started_at).toLocaleString() 
      lastParsingFinished.value = new Date(curr.finished_at).toLocaleString()
  }
)

onMounted(() => {
  store.dispatch(ActionTypes.GET_PARSER_STATUS, null)
  intervalID.value = setInterval(updateStatus, 50000)
})

onBeforeUnmount(() => {
  clearInterval(intervalID.value)
}) 

const toggleMenu = (): void => {
  emit('onToggleMenu');
}

const updateStatus = (): void => {
  store.dispatch(ActionTypes.GET_PARSER_STATUS, null)
}

const exitFromAdmin = () => {
  store.commit(MutationTypes.SET_USER, null)
  localStorage.removeItem("authToken")
  localStorage.removeItem("refreshToken")
  router.push('/login')
}

const links = ref([
  { name: "Скидки", href: "/discount" },
  { name: "Заказы", href: "/" },
  { name: "Запросы на звонки", href: "/call_requests" },
  { name: "Запросы обратной связи", href: "/feedback_requests" },
  { name: "Новости", href: "/articles" },
  { name: "Банеры", href: "/banners" },
  { name: "Партнеры", href: "/partners" },
  { name: "Варианты доставки", href: "/delivery_types" },
  { name: "Настройки", href: "/settings" },
  { name: "Склады", href: "/stocks" },
  { name: "Прайс", href: "/price" },
  { name: "Пользователи", href: "/users" },
]);

</script>

<template>
  <div :class="['sidebar', { sidebar_isopen: openSidebar }]">
    <router-link
      class="sidebar__link"
      v-for="link in links"
      :key="link.name"
      :to="link.href"
      >{{ link.name }}
    </router-link
    >
    <div class="sidebar__link link__hover" @click="exitFromAdmin">Выход</div>
    <div class="sidebar__status">
      <div class="parser">
        <div class="">Парсер статус: </div>
        <div :class="['parser-status', {parser__good: !isFailedParsing}, {parser__bad: isFailedParsing}]"></div>
      </div>
      <div>
        {{ 'Start: ' + lastParsingStarted }}
      </div>
      <div>
        {{ 'Finish: ' + lastParsingFinished }}
      </div>
    </div>
  </div>
  <div v-if = "!openSidebar" class="sidebar-marker" @click="toggleMenu">&#5125;</div>
  <div v-else class="sidebar-marker sidebar-marker_isopen" @click="toggleMenu">&#5130;</div>
</template>

<style lang="scss" scoped>
.router-link-active{
  color:#4275d8;
  text-decoration: underline;
}
.link__hover:hover{
  cursor: pointer;  
}
.parser {
  display: flex;
  justify-content: space-between;
  align-items: center;
  &-status{
    display: inline-block;
    width: 20px;
    height: 20px;
    border-radius: 50%;
  }
  &__good{
    background-color: green;
  }
  &__bad{
    background-color: red;
  }
}
.sidebar {
  left: 0;
  top: 62px;
  height: 100%;
  background: #fff;
  position: fixed;
  width: 250px;
  padding: 20px;
  transition: 0.2s;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.07);
  transform: translateX(-250px);
  &_isopen {
    transform: translateX(0px);
  }
  &__link {
    display: block;
    border-radius: 12px;
    border: 2px solid #fff;
    transition: 0.2s;
    font-weight: bold;
    margin-bottom: 10px;
    &:hover {
      color: var(--primary);
    }
  }
  &__status {
    border-radius: 12px;
    border: 2px solid #fff;
    transition: 0.2s;
    font-weight: bold;
    font-size: 14px;
    margin-top: 50px;
  }
  &-marker {
    position: fixed;
    left: 0;
    width: 15px;
    background: var(--background-content);
    height: 100%;
    top: 62px;
    z-index: 1;
    cursor: pointer;
    color: var(--primary-hover);
    display: flex;
    align-items: center;
    justify-content: center;
    &_isopen{
      left: 235px;      
      background: var(--background);
    }
  }

}
</style>

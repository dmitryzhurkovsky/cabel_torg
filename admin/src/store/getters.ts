import { GetterTree } from 'vuex'
import { IDeliveryType } from '../types'
import { State } from './state'

export type Getters = {
  user(state: State): {[key:string]: any},
  isLoading(sate: State): boolean,
  deliveryTypesData(state: State): Array<IDeliveryType>
  isLogin(state: State): boolean
  articlesData(state: State): Array<IDeliveryType>
  bannersData(state: State): Array<IDeliveryType>
  partnersData(state: State): Array<IDeliveryType>
  callRequests(state: State): Array<IDeliveryType>
  feedbackRequests(state: State): Array<IDeliveryType>
  orders(state: State): Array<IDeliveryType>
  orderList(state: State): Array<IDeliveryType>
  orderTypes(state:State): Array<IDeliveryType>
  isPopUpOpen(state: State): Boolean
  categories(state: State): Array<IDeliveryType>
  activeCategory(state: State): string
  settings(state: State): IDeliveryType
  stocks(state: State): Array<IDeliveryType>
  goods(state: State): Array<IDeliveryType>
  goodsOfset(state: State): number 
  activePage(state: State): number 
  totalPages(state: State): number 
  itemsInPage(state: State): number 
  usersList(state: State): Array<IDeliveryType>
}

export const getters: GetterTree<State, State> & Getters = {
  user: (state) => {
    return state.user
  },
  isLoading: (state) => {
    return state.isLoading
  },
  deliveryTypesData: (state) => {
    return state.deliveryTypesData
  },
  isLogin: (state) => {
    if (!state.user) {
      return false
    } 
    return Boolean(Object.keys(state.user).length)
  },
  articlesData: (state) => {
    return state.articles
  },
  bannersData: (state) => {
    return state.banners
  },
  partnersData: (state) => {
    return state.partners
  },
  callRequests: (state) => {
    return state.callRequests
  },
  feedbackRequests: (state) => {
    return state.feedbackRequests
  },
  orders: (state) => {
    return state.orders
  },
  orderTypes: (state) => {
    return state.orderTypes
  },
  orderList: (state) => {
    const list = [] as Array<IDeliveryType>;
    
    state.orders.forEach(item => {
      const listElement = {} as IDeliveryType
      listElement.id = 'Заказ # ' + item.id 
      listElement.idFromDB = item.id 
      listElement.date = item.created_at.slice(0, 10)
      listElement.status = item.status
      listElement.statusName = state.orderTypes.filter(elem => elem.id === item.status)[0].name
      listElement.total_price = item.total_price
      const isDelivery_type_name = state.deliveryTypesData.filter(elem => elem.id === item.delivery_type_id)[0]
      const delivery_type_name = isDelivery_type_name ? isDelivery_type_name.payload : 'Не определено'
      listElement.delivery_type_name = delivery_type_name
      listElement.delivery_type_id = item.delivery_type_id
      list.push(listElement)
    })
    return list
  },
  isPopUpOpen: (state) => {
    return state.isPopUpOpen
  },
  categories: (state) => {
    return state.categories
  },
  activeCategory: (state) => {
    return state.activeCategory
  },
  settings: (state) => {
    return state.settings
  },
  stocks: (state) => {
    return state.stocks
  },
  goods: (state) => {
    return state.goods
  },
  goodsOfset: (state) => {
    return state.goodsOfset
  },
  activePage: (state) => {
    return state.activePage
  },
  totalPages: (state) => {
    return state.totalPages
  },
  itemsInPage: (state) => {
    return state.itemsInPage
  },
  usersList: (state) => {
    return state.users
  },
}
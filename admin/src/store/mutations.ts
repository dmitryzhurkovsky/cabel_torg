import { MutationTree } from 'vuex';
import { IDeliveryType } from '../types';
import { MutationTypes } from './mutation-types';
import { State } from './state';

export type Mutations<S = State> = {
  [MutationTypes.SET_USER](state: S, payload: any): void,
  [MutationTypes.SET_ERRORS](state: S, payload: any): void,
  [MutationTypes.SET_IS_LOADING](state: S, payload: boolean): void,
  [MutationTypes.SET_DELIVERY_TYPES](state: S, payload: Array<IDeliveryType>): void,
  [MutationTypes.ADD_TO_DELIVERY_TYPES](state: S, payload: IDeliveryType): void,
  [MutationTypes.DELETE_FROM_DELIVERY_TYPES](state: S, payload: number): void,
  [MutationTypes.UPDATE_DELIVERY_TYPES](state: S, payload: IDeliveryType): void,
  [MutationTypes.SET_ARTICLES](state: S, payload: Array<IDeliveryType>): void,
  [MutationTypes.ADD_TO_ARTICLES](state: S, payload: IDeliveryType): void,
  [MutationTypes.DELETE_FROM_ARTICLES](state: S, payload: number): void,
  [MutationTypes.UPDATE_ARTICLE](state: S, payload: IDeliveryType): void,
  [MutationTypes.SET_PARTNERS](state: S, payload: Array<IDeliveryType>): void,
  [MutationTypes.ADD_TO_PARTNERS](state: S, payload: IDeliveryType): void,
  [MutationTypes.DELETE_FROM_PARTNERS](state: S, payload: number): void,
  [MutationTypes.SET_CALL_REQUESTS](state: S, payload: Array<IDeliveryType>): void,
  [MutationTypes.DELETE_FROM_CALL_REQUESTS](state: S, payload: number): void,
  [MutationTypes.SET_FEEDBACK_REQUESTS](state: S, payload: Array<IDeliveryType>): void,
  [MutationTypes.DELETE_FROM_FEEDBACK_REQUESTS](state: S, payload: number): void,
  [MutationTypes.SET_ORDERS](state: S, payload: Array<IDeliveryType>): void,
  [MutationTypes.SET_ISPOPUPOPEN](state: S, payload: boolean): void,
  [MutationTypes.SET_NEW_ORDER_STATUS](state: S, payload: IDeliveryType): void,
  [MutationTypes.SET_CATEGORIES](state: S, payload: Array<IDeliveryType>): void,
  [MutationTypes.UPDATE_CATEGORY](state: S, payload: IDeliveryType): void,
  [MutationTypes.SET_SETTINGS](state: S, payload: IdleDeadline): void,
  [MutationTypes.SET_STOCKS](state: S, payload: Array<IDeliveryType>): void,
  [MutationTypes.ADD_TO_STOCKS](state: S, payload: IDeliveryType): void,
  [MutationTypes.DELETE_FROM_STOCKS](state: S, payload: number): void,
  [MutationTypes.UPDATE_STOCK](state: S, payload: IDeliveryType): void,
  [MutationTypes.SET_BANNERS](state: S, payload: Array<IDeliveryType>): void,
  [MutationTypes.ADD_TO_BANNERS](state: S, payload: IDeliveryType): void,
  [MutationTypes.DELETE_FROM_BANNERS](state: S, payload: number): void,
  [MutationTypes.UPDATE_BANNER](state: S, payload: IDeliveryType): void,
  [MutationTypes.SET_PRODUCTS](state: S, payload: IDeliveryType): void,
  [MutationTypes.SET_PRODUCTS_OFSET](state: S, payload: number): void,
  [MutationTypes.SET_ACTIVE_PAGE](state: S, payload: number): void,
  [MutationTypes.SET_TOTAL_PAGES](state: S, payload: number): void,
  [MutationTypes.SET_ITEMS_IN_PAGE](state: S, payload: number): void,
  [MutationTypes.UPDATE_PRODUCT](state: S, payload: IDeliveryType): void,
  [MutationTypes.SET_USERS_LIST](state: S, payload: Array<IDeliveryType>): void,
}

export const mutations: MutationTree<State> & Mutations = {
  [MutationTypes.SET_USER](state, payload: any) {
    state.user = payload
  },
  [MutationTypes.SET_ERRORS](state, payload: any) {
    state.errors = payload
  },
  [MutationTypes.SET_IS_LOADING](state, payload: boolean) {
    state.isLoading = payload
  },
  [MutationTypes.SET_DELIVERY_TYPES](state, payload: Array<IDeliveryType>) {
    state.deliveryTypesData = payload
  },
  [MutationTypes.ADD_TO_DELIVERY_TYPES](state, payload: IDeliveryType) {
    state.deliveryTypesData = [...state.deliveryTypesData, payload]
  },
  [MutationTypes.DELETE_FROM_DELIVERY_TYPES](state, payload: number) {
    state.deliveryTypesData = state.deliveryTypesData.filter(item => item.id !== payload)
  },
  [MutationTypes.UPDATE_DELIVERY_TYPES](state, payload: IDeliveryType) {
    state.deliveryTypesData = state.deliveryTypesData.filter(item => item.id !== payload.id)
    state.deliveryTypesData.push(payload)
  },
  [MutationTypes.SET_ARTICLES](state, payload: Array<IDeliveryType>) {
    state.articles = payload
  },
  [MutationTypes.ADD_TO_ARTICLES](state, payload: IDeliveryType) {
    state.articles = [...state.articles, payload]
  },
  [MutationTypes.DELETE_FROM_ARTICLES](state, payload: number) {
    state.articles = state.articles.filter(item => item.id !== payload)
  },
  [MutationTypes.UPDATE_ARTICLE](state, payload: IDeliveryType) {
    state.articles = state.articles.filter(item => item.id !== payload.id)
    state.articles.push(payload)
  },
  [MutationTypes.SET_PARTNERS](state, payload: Array<IDeliveryType>) {
    state.partners = payload
  },
  [MutationTypes.ADD_TO_PARTNERS](state, payload: IDeliveryType) {
    state.partners = [...state.partners, payload]
  },
  [MutationTypes.DELETE_FROM_PARTNERS](state, payload: number) {
    state.partners = state.partners.filter(item => item.id !== payload)
  },
  [MutationTypes.SET_CALL_REQUESTS](state, payload: Array<IDeliveryType>) {
    state.callRequests = payload
  },
  [MutationTypes.DELETE_FROM_CALL_REQUESTS](state, payload: number) {
    state.callRequests = state.callRequests.filter(item => item.id !== payload)
  },
  [MutationTypes.SET_FEEDBACK_REQUESTS](state, payload: Array<IDeliveryType>) {
    state.feedbackRequests = payload
  },
  [MutationTypes.DELETE_FROM_FEEDBACK_REQUESTS](state, payload: number) {
    state.feedbackRequests = state.feedbackRequests.filter(item => item.id !== payload)
  },
  [MutationTypes.SET_ORDERS](state, payload: Array<IDeliveryType>) {
    state.orders = payload
  },
  [MutationTypes.SET_ISPOPUPOPEN](state, payload: boolean) {
    state.isPopUpOpen = payload
  },
  [MutationTypes.SET_NEW_ORDER_STATUS](state, payload: IDeliveryType) {
    const without = state.orders.filter(order => order.id !== payload.id)
    state.orders = [...without, payload]
  },
  [MutationTypes.SET_CATEGORIES](state, payload: Array<IDeliveryType>) {
    state.categories = payload
  },
  [MutationTypes.UPDATE_CATEGORY](state, payload: IDeliveryType) {
    const category = state.categories.filter(item => item.id === payload.id)[0]
    if (category) {
      category.discount = payload.discount
    }
  },
  [MutationTypes.SET_SETTINGS](state, payload: IDeliveryType) {
    state.settings = payload
  },
  [MutationTypes.SET_STOCKS](state, payload: Array<IDeliveryType>) {
    state.stocks = payload
  },
  [MutationTypes.ADD_TO_STOCKS](state, payload: IDeliveryType) {
    state.stocks = [...state.stocks, payload]
  },
  [MutationTypes.DELETE_FROM_STOCKS](state, payload: number) {
    state.stocks = state.stocks.filter(item => item.id !== payload)
  },
  [MutationTypes.UPDATE_STOCK](state, payload: IDeliveryType) {
    state.stocks = state.stocks.filter(item => item.id !== payload.id)
    state.stocks.push(payload)
  },
  [MutationTypes.SET_BANNERS](state, payload: Array<IDeliveryType>) {
    state.banners = payload
  },
  [MutationTypes.ADD_TO_BANNERS](state, payload: IDeliveryType) {
    state.banners = [...state.banners, payload]
  },
  [MutationTypes.DELETE_FROM_BANNERS](state, payload: number) {
    state.banners = state.banners.filter(item => item.id !== payload)
  },
  [MutationTypes.UPDATE_BANNER](state, payload: IDeliveryType) {
    state.banners = state.banners.filter(item => item.id !== payload.id)
    state.banners.push(payload)
  },
  [MutationTypes.SET_PRODUCTS](state, payload: IDeliveryType) {
    state.goods = payload.data
    state.totalPages =  Math.ceil(payload.total / payload.limit);    
  },
  [MutationTypes.SET_PRODUCTS_OFSET](state, payload: number) {
    state.goodsOfset = payload
  },
  [MutationTypes.SET_ACTIVE_PAGE](state, payload: number) {
    state.activePage = payload
  },
  [MutationTypes.SET_TOTAL_PAGES](state, payload: number) {
    state.totalPages = payload
  },
  [MutationTypes.SET_ITEMS_IN_PAGE](state, payload: number) {
    state.itemsInPage = payload
  },
  [MutationTypes.UPDATE_PRODUCT](state, payload: IDeliveryType) {
    state.goods = state.goods.filter(item => item.id !== payload.id)
    state.goods.push(payload)
  },
  [MutationTypes.SET_USERS_LIST](state, payload: Array<IDeliveryType>) {
    state.users = payload
  },
}

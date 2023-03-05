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
}

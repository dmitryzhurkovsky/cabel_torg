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
    state.deliveryTypesData.push(payload)
  },
  [MutationTypes.DELETE_FROM_DELIVERY_TYPES](state, payload: number) {
    state.deliveryTypesData = state.deliveryTypesData.filter(item => item.id !== payload)
  },
  [MutationTypes.UPDATE_DELIVERY_TYPES](state, payload: IDeliveryType) {
    state.deliveryTypesData = state.deliveryTypesData.filter(item => item.id !== payload.id)
    state.deliveryTypesData.push(payload)
  },
}

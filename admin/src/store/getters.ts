import { GetterTree } from 'vuex'
import { IDeliveryType } from '../types'
import { State } from './state'

export type Getters = {
  user(state: State): {[key:string]: any},
  isLoading(sate: State): boolean,
  deliveryTypesData(state: State): Array<IDeliveryType>
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
}
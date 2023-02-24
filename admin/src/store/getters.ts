import { GetterTree } from 'vuex'
import { IDeliveryType } from '../types'
import { State } from './state'

export type Getters = {
  user(state: State): {[key:string]: any},
  isLoading(sate: State): boolean,
  deliveryTypesData(state: State): Array<IDeliveryType>
  isLogin(state: State): boolean
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
    console.log('Getter', Boolean(Object.keys(state.user).length));
    return Boolean(Object.keys(state.user).length)
  }
}
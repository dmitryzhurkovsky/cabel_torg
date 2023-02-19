import { ActionTree, ActionContext } from 'vuex'
import { State } from './state'
import { Mutations } from './mutations'
import { ActionTypes } from './action-types'
import { MutationTypes } from './mutation-types'
import axios from "axios";
import { IDeliveryType } from '../types'

type AugmentedActionContext = {
  commit<K extends keyof Mutations>(
    key: K,
    payload: Parameters<Mutations[K]>[1]
  ): ReturnType<Mutations[K]>
} & Omit<ActionContext<State, State>, 'commit'>

export interface Actions {
  [ActionTypes.SEND_USER_REQUEST](
    { commit, dispatch }: AugmentedActionContext,
    payload: any
  ): Promise<any>,
  [ActionTypes.GET_USER_DATA](
    { commit }: AugmentedActionContext
  ): Promise<any>,
  [ActionTypes.GET_DELIVERY_TYPE](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.ADD_DELIVERY_TYPE](
    { commit }: AugmentedActionContext,
    payload: {[key: string]:string}
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.DELETE_DELIVERY_TYPE](
    { commit }: AugmentedActionContext,
    payload: number
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.EDIT_DELIVERY_TYPE](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
}

export const actions: ActionTree<State, State> & Actions = {
  [ActionTypes.SEND_USER_REQUEST]({ commit, dispatch }, payload) {
    return new Promise((resolve) => {
      commit(MutationTypes.SET_ERRORS, {})
      axios.post(import.meta.env.VITE_APP_API_URL + "token", payload).
      then((response) => {
        console.log(response);
        localStorage.setItem("authToken", response.data.access_token);
        localStorage.setItem("refreshToken", response.data.refresh_token);
        dispatch(ActionTypes.GET_USER_DATA, null)
        .then((response) => {
          resolve(response.data);
        })
      });
    }) 
  },

  [ActionTypes.GET_USER_DATA]({ commit }) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "users/mine").
      then((response) => {
        commit(MutationTypes.SET_USER, response.data);
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_DELIVERY_TYPE]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "service_entities/delivery_types").
      then((response) => {
        commit(MutationTypes.SET_DELIVERY_TYPES, response.data);
        resolve(response.data);
      })
    })
  },

  [ActionTypes.ADD_DELIVERY_TYPE]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.post(import.meta.env.VITE_APP_API_URL + "service_entities/delivery_types", payload).
      then((response) => {
        commit(MutationTypes.ADD_TO_DELIVERY_TYPES, response.data);
        resolve(response.data);
      })
    })
  },

  [ActionTypes.DELETE_DELIVERY_TYPE]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.delete(import.meta.env.VITE_APP_API_URL + "service_entities/delivery_types/" + String(payload)).
      then((response) => {
        commit(MutationTypes.DELETE_FROM_DELIVERY_TYPES, payload);
        resolve(response.data);
      })
    })
  },

  [ActionTypes.EDIT_DELIVERY_TYPE]({ commit }, data) {
    return new Promise((resolve) => {
      const params = { payload: data.payload as string}
      axios.patch(import.meta.env.VITE_APP_API_URL + "service_entities/delivery_types/" + String(data.id), params).
      then((response) => {
        commit(MutationTypes.UPDATE_DELIVERY_TYPES, response.data);
        resolve(response.data);
      })
    })
  },
}
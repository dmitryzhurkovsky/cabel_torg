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
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<any>,
  [ActionTypes.GET_DELIVERY_TYPE](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.ADD_DELIVERY_TYPE](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.DELETE_DELIVERY_TYPE](
    { commit }: AugmentedActionContext,
    payload: number
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.EDIT_DELIVERY_TYPE](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_ARTICLE_DATA](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.ADD_ARTICLE](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.DELETE_ARTICLE](
    { commit }: AugmentedActionContext,
    payload: number
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.EDIT_ARTICLE](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.UPLOAD_ARTICLE_PHOTO](
    { commit }: AugmentedActionContext,
    payload: any
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_PARTNERS_DATA](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.ADD_PARTNER](
    { commit }: AugmentedActionContext,
    payload: any
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.DELETE_PARTNER](
    { commit }: AugmentedActionContext,
    payload: number
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_CALL_REQUESTS_DATA](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.DELETE_CALL_REQUEST](
    { commit }: AugmentedActionContext,
    payload: number
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_FEEDBACK_REQUESTS_DATA](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.DELETE_FEEDBACK_REQUEST](
    { commit }: AugmentedActionContext,
    payload: number
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_ORDERS_DATA](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.UPDATE_ORDER_STATUS](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_CATEGORIES_DATA](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.EDIT_CATEGORY_DISCOUNT](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_SETTINGS_DATA](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.EDIT_SETTINGS_DATA](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_STOCKS_DATA](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.ADD_STOCK](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.DELETE_STOCK](
    { commit }: AugmentedActionContext,
    payload: number
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.EDIT_STOCK](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_BANNERS_DATA](
    { commit }: AugmentedActionContext,
    payload: null
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.ADD_BANNER](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.DELETE_BANNER](
    { commit }: AugmentedActionContext,
    payload: number
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.EDIT_BANNER](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.UPLOAD_BANNER_PHOTO](
    { commit }: AugmentedActionContext,
    payload: any
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.GET_PRODUCTS_DATA](
    { commit }: AugmentedActionContext,
    payload: IDeliveryType
  ): Promise<Array<IDeliveryType>>,
  [ActionTypes.EDIT_PRODUCT_DISCOUNT](
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
        localStorage.setItem("authToken", response.data.access_token)
        localStorage.setItem("refreshToken", response.data.refresh_token)
        dispatch(ActionTypes.GET_USER_DATA, null)
        .then((response) => {
          resolve(response.data)
        })
      }).catch((err) => {
        if (err.response.status = 404) {
          resolve({});
        }
        console.log('Send login request ', err)
        
      });
    }) 
  },

  [ActionTypes.GET_USER_DATA]({ commit }) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "users/mine").
      then((response) => {
        if (response.data.is_admin) {
          commit(MutationTypes.SET_USER, response.data)
        } else {
          localStorage.removeItem("authToken")
          localStorage.removeItem("refreshToken")
        }
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_DELIVERY_TYPE]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "service_entities/delivery_types").
      then((response) => {
        commit(MutationTypes.SET_DELIVERY_TYPES, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.ADD_DELIVERY_TYPE]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.post(import.meta.env.VITE_APP_API_URL + "service_entities/delivery_types", payload).
      then((response) => {
        commit(MutationTypes.ADD_TO_DELIVERY_TYPES, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.DELETE_DELIVERY_TYPE]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.delete(import.meta.env.VITE_APP_API_URL + "service_entities/delivery_types/" + String(payload)).
      then((response) => {
        commit(MutationTypes.DELETE_FROM_DELIVERY_TYPES, payload)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.EDIT_DELIVERY_TYPE]({ commit }, data) {
    return new Promise((resolve) => {
      // const params = { payload: data.payload as string}
      axios.patch(import.meta.env.VITE_APP_API_URL + "service_entities/delivery_types/" + String(data.id), data).
      then((response) => {
        commit(MutationTypes.UPDATE_DELIVERY_TYPES, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_ARTICLE_DATA]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "service_entities/articles").
      then((response) => {
        commit(MutationTypes.SET_ARTICLES, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.DELETE_ARTICLE]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.delete(import.meta.env.VITE_APP_API_URL + "service_entities/articles/" + String(payload)).
      then((response) => {
        commit(MutationTypes.DELETE_FROM_ARTICLES, payload)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.ADD_ARTICLE]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.post(import.meta.env.VITE_APP_API_URL + "service_entities/articles", payload).
      then((response) => {
        commit(MutationTypes.ADD_TO_ARTICLES, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.EDIT_ARTICLE]({ commit }, data) {
    return new Promise((resolve) => {
      axios.patch(import.meta.env.VITE_APP_API_URL + "service_entities/articles/" + String(data.id), data).
      then((response) => {
        commit(MutationTypes.UPDATE_ARTICLE, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.UPLOAD_ARTICLE_PHOTO]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.post(import.meta.env.VITE_APP_API_URL + "service_entities/articles/" + payload.id + '/images', payload.data).
      then((response) => {
        commit(MutationTypes.UPDATE_ARTICLE, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_PARTNERS_DATA]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "service_entities/partners").
      then((response) => {
        commit(MutationTypes.SET_PARTNERS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.DELETE_PARTNER]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.delete(import.meta.env.VITE_APP_API_URL + "service_entities/partners/" + String(payload)).
      then((response) => {
        commit(MutationTypes.DELETE_FROM_PARTNERS, payload)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.ADD_PARTNER]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.post(import.meta.env.VITE_APP_API_URL + "service_entities/partners", payload).
      then((response) => {
        commit(MutationTypes.ADD_TO_PARTNERS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_CALL_REQUESTS_DATA]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "service_entities/request_calls?type_of_request_call=U").
      then((response) => {
        commit(MutationTypes.SET_CALL_REQUESTS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.DELETE_CALL_REQUEST]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.delete(import.meta.env.VITE_APP_API_URL + "service_entities/request_calls/" + String(payload)).
      then((response) => {
        commit(MutationTypes.DELETE_FROM_CALL_REQUESTS, payload)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_FEEDBACK_REQUESTS_DATA]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "service_entities/feedbacks").
      then((response) => {
        commit(MutationTypes.SET_FEEDBACK_REQUESTS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.DELETE_FEEDBACK_REQUEST]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.delete(import.meta.env.VITE_APP_API_URL + "service_entities/feedbacks/" + String(payload)).
      then((response) => {
        commit(MutationTypes.DELETE_FROM_FEEDBACK_REQUESTS, payload)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_ORDERS_DATA]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "orders").
      then((response) => {
        commit(MutationTypes.SET_ORDERS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.UPDATE_ORDER_STATUS]({ commit, getters }, payload) {
    return new Promise((resolve) => {
      const orderForUpdate = getters.orders.filter((item: IDeliveryType) => item.id === payload.orderId)[0]
      axios.patch(import.meta.env.VITE_APP_API_URL + "orders/" + payload.orderId, {status: payload.newStatus}).
      then((response) => {
        orderForUpdate.status = payload.newStatus
        commit(MutationTypes.SET_NEW_ORDER_STATUS, orderForUpdate)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_CATEGORIES_DATA]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "categories").
      then((response) => {
        commit(MutationTypes.SET_CATEGORIES, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.EDIT_CATEGORY_DISCOUNT]({ commit, dispatch }, data) {
    return new Promise((resolve) => {
      const { category, discount } = data
      axios.patch(import.meta.env.VITE_APP_API_URL + "categories/" + category.id, { discount }).
      then((response) => {
        commit(MutationTypes.UPDATE_CATEGORY, response.data)
        dispatch(ActionTypes.GET_PRODUCTS_DATA, data.category)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_SETTINGS_DATA]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "service_entities/vendor_info/1").
      then((response) => {
        commit(MutationTypes.SET_SETTINGS, response.data)
        resolve(response.data);
      })
    })
  },
  
  [ActionTypes.EDIT_SETTINGS_DATA]({ commit }, data) {
    return new Promise((resolve) => {
      axios.patch(import.meta.env.VITE_APP_API_URL + "service_entities/vendor_info/1", data).
      then((response) => {
        commit(MutationTypes.SET_SETTINGS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_STOCKS_DATA]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "service_entities/vendor_info/1/addresses").
      then((response) => {
        commit(MutationTypes.SET_STOCKS, response.data)
        resolve(response.data);
      })
    })
  },
  
  [ActionTypes.DELETE_STOCK]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.delete(import.meta.env.VITE_APP_API_URL + "service_entities/vendor_info/1/addresses/" + String(payload)).
      then((response) => {
        commit(MutationTypes.DELETE_FROM_STOCKS, payload)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.ADD_STOCK]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.post(import.meta.env.VITE_APP_API_URL + "service_entities/vendor_info/1/addresses", payload).
      then((response) => {
        commit(MutationTypes.ADD_TO_STOCKS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.EDIT_STOCK]({ commit }, data) {
    return new Promise((resolve) => {
      axios.patch(import.meta.env.VITE_APP_API_URL + "service_entities/vendor_info/1/addresses/" + String(data.id), data).
      then((response) => {
        commit(MutationTypes.UPDATE_STOCK, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_BANNERS_DATA]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "service_entities/banners").
      then((response) => {
        commit(MutationTypes.SET_BANNERS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.DELETE_BANNER]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.delete(import.meta.env.VITE_APP_API_URL + "service_entities/banners/" + String(payload)).
      then((response) => {
        commit(MutationTypes.DELETE_FROM_BANNERS, payload)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.ADD_BANNER]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.post(import.meta.env.VITE_APP_API_URL + "service_entities/banners", payload).
      then((response) => {
        commit(MutationTypes.ADD_TO_BANNERS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.EDIT_BANNER]({ commit }, data) {
    return new Promise((resolve) => {
      axios.patch(import.meta.env.VITE_APP_API_URL + "service_entities/banners/" + String(data.id), data).
      then((response) => {
        commit(MutationTypes.UPDATE_BANNER, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.UPLOAD_BANNER_PHOTO]({ commit }, payload) {
    return new Promise((resolve) => {
      axios.post(import.meta.env.VITE_APP_API_URL + "service_entities/banners/" + payload.id + '/images', payload.data).
      then((response) => {
        commit(MutationTypes.UPDATE_BANNER, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.GET_PRODUCTS_DATA]({ commit, getters }, params) {
    return new Promise((resolve) => {
      axios.get(import.meta.env.VITE_APP_API_URL + "products?category_id=" + 
        params.id + 
        "&offset=" + getters.goodsOfset +
        "&limit=" + getters.itemsInPage
      ).then((response) => {
        commit(MutationTypes.SET_PRODUCTS, response.data)
        resolve(response.data);
      })
    })
  },

  [ActionTypes.EDIT_PRODUCT_DISCOUNT]({ commit }, data) {
    const { product, discount } = data
    return new Promise((resolve) => {
      axios.patch(import.meta.env.VITE_APP_API_URL + "products/" + String(product.id), { discount }).
      then((response) => {
        commit(MutationTypes.UPDATE_PRODUCT, response.data)
        resolve(response.data);
      })
    })
  },
}
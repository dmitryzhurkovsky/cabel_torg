import axios from "axios";

export default {
  namespaced: true,

  state: {
    favorites: [],
    fullFavorites: [],
  },

  getters: {
    FAVORITES(state) {
      return state.favorites;
    },

    FULL_FAVORITES(state) {
      return state.fullFavorites;
    },
  },

  mutations: {
    SET_FAVORITES(state, payload) {
      state.favorites = payload;
    },

    ADD_TO_FULL_FAVORITES(state, payload) {
      state.fullFavorites.push(payload);
    },

    CLEAR_FULL_FAVORITES(state) {
      state.fullFavorites = [];
    },

    ADD_ITEM_TO_FAVORITE(state, payload) {
        const isItemInFavorite = state.favorites.filter(item => item.product.id === payload.product.id);
        if (!isItemInFavorite.length) {
            state.favorites.push(payload);
        }
    },

    REMOVE_ITEM_FROM_FAVORITE(state, payload) {
        const filteredItemsInFavorite = state.favorites.filter(item => item.product.id !== payload.product.id);
        state.favorites = [...filteredItemsInFavorite];
    },

  },

  actions: {
    async GET_USER_FAVORITE({ commit } ) {
        if (localStorage.getItem("authToken")) {
            try {
              const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'watch_lists/mine/products');
              commit("SET_FAVORITES", response.data);
            } catch (e) {
              console.log(e);
              // commit('notification/ADD_MESSAGE', {name: 'Не возможно обновить избранное', icon: "error", id: '1'}, {root: true})
            }
        } else {
            const isFavoritesInStore = localStorage.getItem('favorites');
            const favoritesInStore = isFavoritesInStore ? JSON.parse(isFavoritesInStore) : [];
            commit("SET_FAVORITES", favoritesInStore);
        }
    },

    async GET_USER_FULL_FAVORITES ({ commit, getters }) {
      getters.FAVORITES.forEach( async item => {
        try {
          const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'products/' + item.product.id);
          commit("ADD_TO_FULL_FAVORITES", response.data);
        } catch (e) {
          console.log(e);
          // commit('notification/ADD_MESSAGE', {name: 'Не возможно обновить избранное', icon: "error", id: '1'}, {root: true})
        }  
      }) 
    },

    async UPDATE_IS_WISH_IN_CART({ commit, dispatch, getters, rootGetters }, data) {
        const type = data.type; 
        const itemData = JSON.parse(JSON.stringify(data.itemData));
        const product = itemData.product;
        if (rootGetters['auth/USER']) {
            // обновим базу
            if (type === 'set') {
              const isPresentFavoriteInStore = getters.FAVORITES.filter(item => item.product.id === product.id);
              if (!isPresentFavoriteInStore.length) {
                  await dispatch("ADD_FAVORITE_TO_DB", { product } );
              }
            } else if (type === 'remove') {
              const isPresentFavoriteInStore = getters.FAVORITES.filter(item => item.product.id === product.id);
              if (isPresentFavoriteInStore.length) {
                  await dispatch("DELETE_FAVORITE_FROM_DB", { product } )
              }    
            }
        } else {
            // обновим localStorage
            const isFavoritesInStore = localStorage.getItem('favorites');
            const favoritesInStore = isFavoritesInStore ? JSON.parse(isFavoritesInStore) : [];
            if (type === 'set') {
                const isPresentFavoriteInStore = favoritesInStore.filter(item => item.product.id === product.id);
                if (!isPresentFavoriteInStore.length) {
                    favoritesInStore.push( { product } );
                    localStorage.setItem('favorites', JSON.stringify(favoritesInStore));
                    commit("ADD_ITEM_TO_FAVORITE", { product } );
                }
            } else if (type === 'remove') {
                const isPresentFavoriteInStore = favoritesInStore.filter(item => item.product.id === product.id);
                if (isPresentFavoriteInStore.length) {
                    const otherFavorites = favoritesInStore.filter(item => item.product.id !== product.id);
                    localStorage.setItem('favorites', JSON.stringify([...otherFavorites]));
                    commit("REMOVE_ITEM_FROM_FAVORITE", itemData);
                }
            }             
        }
    },

    async MERGE_USER_FAVORITES_AND_LOCAL_STORAGE({ commit, dispatch, getters, rootGetters }) {
      if (rootGetters['auth/USER']) {
        try {
            const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'watch_lists/mine/products');
            const itemsFromDB = response.data;
            const newItemsFromDB = [];
            itemsFromDB.forEach( dbItem => {
                const isCommonItem = getters.FAVORITES.filter( siteItem => siteItem.product.id === dbItem.product.id);
                if (isCommonItem.length) {
                    const storage = JSON.parse(localStorage.getItem('favorites'));
                    const otherItemsInStor = storage.filter(item => item.product.id !== isCommonItem[0].product.id);
                    localStorage.setItem('favorites', JSON.stringify(otherItemsInStor))
                } else {
                    newItemsFromDB.push({ product: dbItem.product});
                }
            });
            newItemsFromDB.forEach( async newItem => {
                await commit("ADD_ITEM_TO_FAVORITE", { product: newItem.product } );
            });
            const newItemsFromSite = JSON.parse(localStorage.getItem('favorites'));
            if (newItemsFromSite.length) {
                newItemsFromSite.forEach( async newItem => {
                    await dispatch("ADD_FAVORITE_TO_DB", newItem );
                    const storage = JSON.parse(localStorage.getItem('favorites'));
                    const otherItemsInStor = storage.filter(item => item.product.id !== newItem.product.id);
                    localStorage.setItem('favorites', JSON.stringify([ ...otherItemsInStor ]));
                })
            }  
        } catch (e) {
          console.log(e);
          // commit("notification/ADD_MESSAGE", {name: "Не возможно обновить корзину", icon: "error", id: '1'}, {root: true})
        }
      }
    },

    async DELETE_FAVORITE_FROM_DB({ commit, rootGetters }, itemData ) {
      if (rootGetters['auth/USER']) {
          try {
              await axios.delete(useRuntimeConfig().public.NUXT_APP_API_URL + 'watch_lists/mine/products/' + itemData.product.id);
              commit("REMOVE_ITEM_FROM_FAVORITE", { product: itemData.product});
          } catch (e) {
              console.log(e);
              // commit("notification/ADD_MESSAGE", {name: "Не возможно обновить в корзине " + itemData.product.name, icon: "error", id: '1'}, {root: true})
          }
      }
    },

    async ADD_FAVORITE_TO_DB({ commit, rootGetters }, itemData ) {
      if (rootGetters['auth/USER']) {
          try {
              await axios.post(useRuntimeConfig().public.NUXT_APP_API_URL + 'watch_lists/mine/products/', { product_id: itemData.product.id });
              commit("ADD_ITEM_TO_FAVORITE", { product: itemData.product });
          } catch (e) {
              console.log(e);
              // commit("notification/ADD_MESSAGE", {name: "Не возможно обновить в корзине " + itemData.product.name, icon: "error", id: '1'}, {root: true})
          }
      }
    },

  }
}
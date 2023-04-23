import axios from "axios";

export default {
  namespaced: true,

  state: {
    orders: [],
    orderDocumrnts: [],
    isApplicationOpen: false,
    deliveryTypes: [],
  },

    getters: {
      ORDERS(state) {
        return state.orders;
      },
      TOTAL_ORDER_COST(state) {
        let totalOrderCost = 0;
        state.orders.forEach(item => {
          const curPrice = item.product.price_with_discount_and_tax && item.product.price_with_discount_and_tax !== item.product.price_with_tax 
            ? item.product.price_with_discount_and_tax 
            : item.product.price_with_tax;
          totalOrderCost = Number(totalOrderCost) + Number((item.amount * curPrice).toFixed(2))
        });
        return Number(totalOrderCost.toFixed(2));
      },
      TOTAL_ORDER_QUANTITY(state) {
        return state.orders.length;
      },
      IS_APPLICATION_OPEN(state) {
          return state.isApplicationOpen;
      },
      ORDER_DOCUMENTS(state) {
        return state.orderDocumrnts;
      }
      ,ORDER_DELIVERY_TYPES(state) {
        return state.deliveryTypes;
      }
    },

    mutations: {
      SET_ORDERS(state, orders){
        state.orders = orders;
      },
  
      SET_IS_APPLICATION_OPEN(state, status){
        state.isApplicationOpen = status;
      },

      ADD_ITEM_TO_CART(state, item) {
        const isItemInCart = state.orders.filter(element => element.product.id === item.product.id);
        if (isItemInCart.length) {
          isItemInCart[0].amount = isItemInCart[0].amount + item.amount;
        } else {
          state.orders.push(item);
        }
      },

      UPDATE_ITEM_IN_CART(state, item){
        const isItemInCart = state.orders.filter(element => element.product.id === item.product.id);
        if (isItemInCart.length) {
          isItemInCart[0].amount = item.amount;
        } else {
          state.orders.push(item);
        }
      },
      
      REMOVE_ITEM_FROM_CART(state, item) {
          const filteredItemsInCart = state.orders.filter(element => element.product.id !== item.product.id);
          state.orders = [...filteredItemsInCart];
      },

      SET_ORDER_DOCUMENTS(state, documents){
        state.orderDocumrnts = documents;
      },

      CLEAR_ORDER_DOCUMENTS(state){
        state.orderDocumrnts = [];
      },

      SET_ORDER_DELIVERY_TYPES(state, deliveryTypes){
        state.deliveryTypes = deliveryTypes;
      }
    },

    actions: {
      async GET_USER_ORDER({ commit } ){
          if (localStorage.getItem("authToken")) {
              try {
                const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'carts/mine/products');
                commit("SET_ORDERS", response.data);
              } catch (e) {
                console.log(e);
                commit("notification/ADD_MESSAGE", {name: "Не возможно обновить корзину", icon: "error", id: '1'}, {root: true})
              }
          } else {
              const isCartsInStore = localStorage.getItem('carts');
              const cartsInStore = isCartsInStore ? JSON.parse(isCartsInStore) : [];
              commit("SET_ORDERS", cartsInStore);
          }
      },

      async UPDATE_ITEMS_IN_CART({ commit, dispatch, getters, rootGetters }, data) {
        const type = data.type; 
        const itemData =JSON.parse(JSON.stringify(data.itemData));;
        const product = itemData.product;
        if (rootGetters['auth/USER']) {
            // обновим базу
            if (type === 'increase') {
                const isPresentCartInStore = getters.ORDERS.filter(item => item.product.id === product.id);
                if (isPresentCartInStore.length) {
                    const updatedCart = isPresentCartInStore[0];
                    updatedCart.amount++
                    await dispatch("UPDATE_ITEM_IN_DB", { amount: updatedCart.amount, product: updatedCart.product } ); 
                } else {
                    await dispatch("ADD_ITEM_TO_DB", { amount: 1, product: product } );
                }
            } else if (type ==='decrease') {
                const isPresentCartInStore = getters.ORDERS.filter(item => item.product.id === product.id);
                if (isPresentCartInStore.length) {
                    const updatedCart = isPresentCartInStore[0];
                    if (updatedCart.amount === 1) {
                        await dispatch("DELETE_ITEM_FROM_DB", { amount: updatedCart.amount, product: updatedCart.product } )
                    } else {
                        updatedCart.amount--;
                        await dispatch("UPDATE_ITEM_IN_DB", { amount: updatedCart.amount, product: updatedCart.product } );
                    }
                }    
            } else if (type === 'remove') {
                await dispatch("DELETE_ITEM_FROM_DB", itemData );
            } else if (type === 'set') {
                const isPresentCartInStore = getters.ORDERS.filter(item => item.product.id === product.id);
                if (isPresentCartInStore.length) {
                    const updatedCart = isPresentCartInStore[0];
                    updatedCart.amount = itemData.amount
                    await dispatch("UPDATE_ITEM_IN_DB", { amount: updatedCart.amount, product: updatedCart.product } ); 
                } else {
                    await dispatch("ADD_ITEM_TO_DB", { amount: itemData.amount, product: product } );
                }
            }
        } else {
            // обновим localStorage
            const isCartsInStore = localStorage.getItem('carts');
            const cartsInStore = isCartsInStore ? JSON.parse(isCartsInStore) : [];
            if (type === 'increase') {
                const isPresentCartInStore = cartsInStore.filter(item => item.product.id === product.id);
                if (isPresentCartInStore.length) {
                    const updatedCart = isPresentCartInStore[0];
                    updatedCart.amount++
                    const otherCarts = cartsInStore.filter(item => item.product.id !== product.id);
                    localStorage.setItem('carts', JSON.stringify([...otherCarts, updatedCart]));
                } else {
                    cartsInStore.push({ amount : 1, product });
                    localStorage.setItem('carts', JSON.stringify(cartsInStore));
                }
                commit("ADD_ITEM_TO_CART", { amount: 1, product } );
            } else if (type === 'decrease') {
                const isPresentCartInStore = cartsInStore.filter(item => item.product.id === product.id);
                if (isPresentCartInStore.length) {
                    const updatedCart = isPresentCartInStore[0];
                    const otherCarts = cartsInStore.filter(item => item.product.id !== product.id);
                    if (updatedCart.amount === 1) {
                        localStorage.setItem('carts', JSON.stringify([...otherCarts]));
                        commit("REMOVE_ITEM_FROM_CART", itemData);
                    } else {
                      updatedCart.amount--;
                      localStorage.setItem('carts', JSON.stringify([...otherCarts, updatedCart]));
                      commit("ADD_ITEM_TO_CART", { amount: -1, product } );
                    }
                }
            } else if (type === 'remove') {
                const otherCarts = cartsInStore.filter(item => item.product.id !== product.id);
                localStorage.setItem('carts', JSON.stringify([...otherCarts]));
                commit("REMOVE_ITEM_FROM_CART", itemData);
            } else if (type === 'set') {
                const isPresentCartInStore = cartsInStore.filter(item => item.product.id === product.id);
                const otherCarts = cartsInStore.filter(item => item.product.id !== product.id);
                if (isPresentCartInStore.length) {
                    const updatedCart = isPresentCartInStore[0];
                    if (itemData.amount !== 0) {
                        updatedCart.amount = itemData.amount;
                        const otherCarts = cartsInStore.filter(item => item.product.id !== product.id);
                        localStorage.setItem('carts', JSON.stringify([...otherCarts, updatedCart]));
                        commit("UPDATE_ITEM_IN_CART", itemData);
                    } else {
                        localStorage.setItem('carts', JSON.stringify([...otherCarts]));
                        commit("REMOVE_ITEM_FROM_CART", itemData);
                    }
                } else {
                    const payload = { amount : itemData.amount, product };
                    cartsInStore.push(payload);
                    localStorage.setItem('carts', JSON.stringify(cartsInStore));
                    commit("ADD_ITEM_TO_CART", payload);
                }
            }
        };
      },

      async MERGE_USER_OREDRS_AND_LOCAL_STORAGE({ commit, dispatch, getters, rootGetters }) {
          if (rootGetters['auth/USER']) {
              try {
                  const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'carts/mine/products');
                  const itemsFromDB = response.data;
                  const newItemsFromDB = [];
                  itemsFromDB.forEach( dbItem => {
                      const isCommonItem = getters.ORDERS.filter( siteItem => siteItem.product.id === dbItem.product.id);
                      if (isCommonItem.length) {
                          const newAmount = isCommonItem[0].amount + dbItem.amount;
                          dispatch("UPDATE_ITEM_IN_DB", { amount: newAmount, product: dbItem.product } );
                          const storage = JSON.parse(localStorage.getItem('carts'));
                          const otherItemsInStor = storage.filter(item => item.product.id !== isCommonItem[0].product.id);
                          localStorage.setItem('carts', JSON.stringify(otherItemsInStor))
                      } else {
                          newItemsFromDB.push({ amount: dbItem.amount, product: dbItem.product});
                      }
                  });
                  newItemsFromDB.forEach( async newItem => {
                      await commit("UPDATE_ITEM_IN_CART", { amount: newItem.amount , product: newItem.product } );
                  });
                  const newItemsFromSite = JSON.parse(localStorage.getItem('carts'));
                  if (newItemsFromSite.length) {
                      newItemsFromSite.forEach( async newItem => {
                          await dispatch("ADD_ITEM_TO_DB", newItem );
                          const storage = JSON.parse(localStorage.getItem('carts'));
                          const otherItemsInStor = storage.filter(item => item.product.id !== newItem.product.id);
                          localStorage.setItem('carts', JSON.stringify([ ...otherItemsInStor ]));
                      })
                  }  
              } catch (e) {
                console.log(e);
                commit("notification/ADD_MESSAGE", {name: "Не возможно обновить корзину", icon: "error", id: '1'}, {root: true})
              }
          }
      },

      async DELETE_ITEM_FROM_DB({ commit, rootGetters }, itemData ) {
          if (rootGetters['auth/USER']) {
              try {
                  await axios.delete(useRuntimeConfig().public.NUXT_APP_API_URL + 'carts/mine/products/' + itemData.product.id);
                  commit("REMOVE_ITEM_FROM_CART", {amount : itemData.amount, product: itemData.product});
              } catch (e) {
                  console.log(e);
                  commit("notification/ADD_MESSAGE", {name: "Не возможно обновить в корзине " + itemData.product.name, icon: "error", id: '1'}, {root: true})
              }
          }
      },

      async UPDATE_ITEM_IN_DB({ commit, rootGetters }, itemData ) {
          if (rootGetters['auth/USER']) {
              try {
                  const response = await axios.patch(useRuntimeConfig().public.NUXT_APP_API_URL + 'carts/mine/products/' + itemData.product.id, itemData);
                  commit("UPDATE_ITEM_IN_CART", {amount : response.data.amount, product: itemData.product});
              } catch (e) {
                  console.log(e);
                  commit("notification/ADD_MESSAGE", {name: "Не возможно обновить в корзине " + itemData.product.name, icon: "error", id: '1'}, {root: true})
              }
          }
      },

      async ADD_ITEM_TO_DB({ commit, rootGetters }, itemData ) {
          if (rootGetters['auth/USER']) {
              try {
                  const response = await axios.post(useRuntimeConfig().public.NUXT_APP_API_URL + 'carts/mine/products/', { product_id: itemData.product.id, amount: itemData.amount });
                  commit("UPDATE_ITEM_IN_CART", { amount : response.data.amount, product: itemData.product });
              } catch (e) {
                  console.log(e);
                  commit("notification/ADD_MESSAGE", {name: "Не возможно обновить в корзине " + itemData.product.name, icon: "error", id: '1'}, {root: true})
              }
          }
      },

      async SEND_ORDER_REQUEST({ commit, dispatch, rootGetters, getters }, itemData ) {
        // if (rootGetters['auth/USER']) {
            try {
                const response = await axios.post(useRuntimeConfig().public.NUXT_APP_API_URL + 'orders', itemData);
                // commit("UPDATE_ITEM_IN_CART", { amount : response.data.amount, product: itemData.product });
                commit("header/SET_POPUP_ACTION", 'ShowCompleteMsg', {root: true});
                const msg ={};
                msg.main = 'Наш менеджер свяжется с вами в ближайшее время.';
                msg.bolt = 'Время работы:';
                msg.sub = ' Пн-Пт - 9:00 - 17:00'
                commit("header/SET_POPUP_MESSAGE", msg, {root: true});
                commit("header/SET_IS_POPUP_OPEN", true, {root: true});
                getters.ORDERS.forEach(async item => {
                  await dispatch("DELETE_ITEM_FROM_DB", item );
                  commit("REMOVE_ITEM_FROM_CART", item);
                })
                // commit("SET_ORDERS", []);
                commit("SET_IS_APPLICATION_OPEN", false);
                commit("profile/CHANGE_SCREEN", 0, {root: true});
            } catch (e) {
                console.log(e);
                commit("notification/ADD_MESSAGE", {name: "Не возможно отправить заказ", icon: "error", id: '1'}, {root: true})
            }
        // }
      },

      async GET_ORDER_DOCUMENTS({ commit } ){
        try {
            const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'orders/mine');
            commit("SET_ORDER_DOCUMENTS", response.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно обновить заказы", icon: "error", id: '1'}, {root: true})
        }
      },

      async GET_ORDER_DELIVERY_TYPES({ commit } ){
        try {
            const response = await axios.get(useRuntimeConfig().public.NUXT_APP_API_URL + 'service_entities/delivery_types');
            commit("SET_ORDER_DELIVERY_TYPES", response.data);
        } catch (e) {
            console.log(e);
            commit("notification/ADD_MESSAGE", {name: "Не возможно обновить способы доставки", icon: "error", id: '1'}, {root: true})
        }
      },
      
    }
  };

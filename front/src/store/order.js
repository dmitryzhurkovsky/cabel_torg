import axios from "axios";

export default {
  namespaced: true,

  state: {
    orders: [],
    isApplicationOpen: false,
  },

    getters: {
      ORDERS(state) {
        return state.orders;
      },
      TOTAL_ORDER_COST(state) {
        let totalOrderCost = 0;
        state.orders.forEach(item => {totalOrderCost = Number(totalOrderCost) + Number((item.amount * item.product.price).toFixed(2))});
        return totalOrderCost;
      },
      TOTAL_ORDER_QUANTITY(state) {
        const position = state.orders.length;
        let totalGoods = 0;
        state.orders.forEach(item => {totalGoods = totalGoods + item.amount});
        return 'позиций - ' + position + ' (товаров ' + totalGoods + ')';
      },
      IS_APPLICATION_OPEN(state) {
          return state.isApplicationOpen;
      }
    },

    mutations: {
      SET_ORDERS(state, payload){
        state.orders = payload;
      },
  
      SET_IS_APPLICATION_OPEN(state, payload){
        state.isApplicationOpen = payload;
      },

      ADD_ITEM_TO_CART(state, payload) {
        const isItemInCart = state.orders.filter(item => item.product.id === payload.product.id);
        if (isItemInCart.length) {
          isItemInCart[0].amount = isItemInCart[0].amount + payload.amount;
        } else {
          state.orders.push(payload);
        }
      },

      UPDATE_ITEM_IN_CART(state, payload){
        const isItemInCart = state.orders.filter(item => item.product.id === payload.product.id);
        if (isItemInCart.length) {
          isItemInCart[0].amount = payload.amount;
        } else {
          state.orders.push(payload);
        }
      },
      
      REMOVE_ITEM_FROM_CART(state, payload) {
          const filteredItemsInCart = state.orders.filter(item => item.product.id !== payload.product.id);
          state.orders = [...filteredItemsInCart];
      },

    },

    actions: {
      async GET_USER_ORDER({ commit, rootGetters } ){
          if (rootGetters['auth/USER']) {
              try {
                const response = await axios.get(process.env.VUE_APP_API_URL + 'carts/mine/products');
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
        const itemData = JSON.parse(JSON.stringify(data.itemData));
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
                    console.log('карточка для обновления', updatedCart);
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
                  const response = await axios.get(process.env.VUE_APP_API_URL + 'carts/mine/products');
                  const itemsFromDB = response.data;
                  const newItemsFromDB = [];
                  const commonItems = [];
                  itemsFromDB.forEach( async dbItem => {
                      const isCommonItem = getters.ORDERS.filter( siteItem => siteItem.product.id === dbItem.product.id);
                      if (commonItems.length) {
                          const newAmount = Number((Number(isCommonItem.amount) + Number(dbItem.amount)).toFixed(2));
                          await dispatch("UPDATE_ITEM_IN_DB", { amount: newAmount, product: isCommonItem.product } );
                          const storage = JSON.parse(localStorage.getItem('carts'));
                          const otherItemsInStor = storage.filter(item => item.product.id !== isCommonItem.product.id);
                          localStorage.setItem(JSON.stringify([ ...otherItemsInStor ]));
                      } else {
                          newItemsFromDB.push({ amount: dbItem.amount, product: dbItem.product});
                      }
                  });
                  newItemsFromDB.forEach( async newItem => {
                      console.log('new ', newItem);
                      await commit("UPDATE_ITEM_IN_CART", { amount: newItem.amount , product: newItem.product } );
                  });
                  const newItemsFromSite = JSON.parse(localStorage.getItem('carts'));
                  if (newItemsFromSite.length) {
                      newItemsFromSite.forEach( async newItem => {
                          await dispatch("ADD_ITEM_TO_DB", newItem );
                          const storage = JSON.parse(localStorage.getItem('carts'));
                          const otherItemsInStor = storage.filter(item => item.product.id !== newItem.product.id);
                          localStorage.setItem(JSON.stringify([ ...otherItemsInStor ]));
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
                  await axios.delete(process.env.VUE_APP_API_URL + 'carts/mine/products/' + itemData.product.id);
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
                  const response = await axios.patch(process.env.VUE_APP_API_URL + 'carts/mine/products/' + itemData.product.id, 
                    { amount : itemData.amount, product: itemData.product }
                  );
                  console.log('SSSS ', response);
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
                  const response = await axios.post(process.env.VUE_APP_API_URL + 'carts/mine/products/', { product_id: itemData.product.id, amount: itemData.amount });
                  commit("UPDATE_ITEM_IN_CART", { amount : response.data.amount, product: itemData.product });
              } catch (e) {
                  console.log(e);
                  commit("notification/ADD_MESSAGE", {name: "Не возможно обновить в корзине " + itemData.product.name, icon: "error", id: '1'}, {root: true})
              }
          }
      },

    }
  };

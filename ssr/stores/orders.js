import axios from "@/utils/api";
import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import { useNotificationsStore } from "@/stores/notifications";
import { useAuthStore } from "@/stores/auth";
import { useHeaderStore } from "@/stores/header";
import { useProfileStore } from '@/stores/profile';

export const useOrdersStore = defineStore ('ordersStore', () => {

  const notificationsStore = useNotificationsStore();
  const authStore = useAuthStore();
  const headerStore = useHeaderStore();
  const profileStore = useProfileStore();

  const orders = ref([]);
  const orderDocuments = ref([]);
  const deliveryTypes = ref([]);
  const isApplicationOpen = ref(false);

  const totalOrderCost = computed(() => {
    let totalOrderCost = 0;
    orders.value.forEach(item => {
      const curPrice = item.product.price_with_discount_and_tax && item.product.price_with_discount_and_tax !== item.product.price_with_tax 
        ? item.product.price_with_discount_and_tax 
        : item.product.price_with_tax;
      totalOrderCost = Number(totalOrderCost) + Number((item.amount * curPrice).toFixed(2))
    });
    return Number(totalOrderCost.toFixed(2));
  });

  const totalOrderQuantity = computed(() => {
    return orders.value.length;
  });

  const getOrderDeliveryTypes = async () => {
    try {
        const response = await axios.get('service_entities/delivery_types');
        deliveryTypes.value = response.data;
    } catch (e) {
        console.log(e);
      // notificationsStore.addMessage({name: "Не возможно обновить способы доставки " + e, icon: "error", id: '1'});
    }
  };

  const setIsApplicationOpen = (status) => {
    isApplicationOpen.value = status;
  };

  const clearOrders = () => {
    orders.value = [];
  };

  const getUserOrder = async () => {
    if (localStorage.getItem("authToken")) {
      try {
        const response = await axios.get('carts/mine/products');
        orders.value = response.data;
      } catch (e) {
        console.log(e);
      // notificationsStore.addMessage({name: "Не возможно обновить корзину" + e, icon: "error", id: '1'});
      }
    } else {
      const isCartsInStore = localStorage.getItem('carts');
      const cartsInStore = isCartsInStore ? JSON.parse(isCartsInStore) : [];
      orders.value = cartsInStore;
    }
  };

  const updateItemsInCart = async (data) => {
    const type = data.type; 
    const itemData = JSON.parse(JSON.stringify(data.itemData));;
    const product = itemData.product;
    if (authStore.userData) {
        // обновим базу
        if (type === 'increase') {
            const isPresentCartInStore = orders.value.filter(item => item.product.id === product.id);
            if (isPresentCartInStore.length) {
                const updatedCart = isPresentCartInStore[0];
                updatedCart.amount++;
                await updateItemInDB({ amount: updatedCart.amount, product: updatedCart.product });
            } else {
                await addItemToDB({ amount: 1, product: product });
            }
        } else if (type ==='decrease') {
            const isPresentCartInStore = orders.value.filter(item => item.product.id === product.id);
            if (isPresentCartInStore.length) {
                const updatedCart = isPresentCartInStore[0];
                if (updatedCart.amount === 1) {
                  await deleteItemsFromDB({ amount: updatedCart.amount, product: updatedCart.product });
                } else {
                  updatedCart.amount--;
                  await updateItemInDB({ amount: updatedCart.amount, product: updatedCart.product });
                }
            }    
        } else if (type === 'remove') {
          await deleteItemsFromDB(itemData);
        } else if (type === 'set') {
            const isPresentCartInStore = orders.value.filter(item => item.product.id === product.id);
            if (isPresentCartInStore.length) {
                const updatedCart = isPresentCartInStore[0];
                updatedCart.amount = itemData.amount
                await updateItemInDB({ amount: updatedCart.amount, product: updatedCart.product });
            } else {
                await addItemToDB({ amount: itemData.amount, product: product });
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
            addItemToCart({ amount: 1, product });
        } else if (type === 'decrease') {
            const isPresentCartInStore = cartsInStore.filter(item => item.product.id === product.id);
            if (isPresentCartInStore.length) {
                const updatedCart = isPresentCartInStore[0];
                const otherCarts = cartsInStore.filter(item => item.product.id !== product.id);
                if (updatedCart.amount === 1) {
                    localStorage.setItem('carts', JSON.stringify([...otherCarts]));
                    removeItemFromCart(itemData)
                } else {
                  updatedCart.amount--;
                  localStorage.setItem('carts', JSON.stringify([...otherCarts, updatedCart]));
                  addItemToCart({ amount: -1, product });
                }
            }
        } else if (type === 'remove') {
            const otherCarts = cartsInStore.filter(item => item.product.id !== product.id);
            localStorage.setItem('carts', JSON.stringify([...otherCarts]));
            removeItemFromCart(itemData);
        } else if (type === 'set') {
            const isPresentCartInStore = cartsInStore.filter(item => item.product.id === product.id);
            const otherCarts = cartsInStore.filter(item => item.product.id !== product.id);
            if (isPresentCartInStore.length) {
                const updatedCart = isPresentCartInStore[0];
                if (itemData.amount !== 0) {
                    updatedCart.amount = itemData.amount;
                    const otherCarts = cartsInStore.filter(item => item.product.id !== product.id);
                    localStorage.setItem('carts', JSON.stringify([...otherCarts, updatedCart]));
                    updateItemInCart(itemData);
                } else {
                    localStorage.setItem('carts', JSON.stringify([...otherCarts]));
                    removeItemFromCart(itemData);
                }
            } else {
                const payload = { amount : itemData.amount, product };
                cartsInStore.push(payload);
                localStorage.setItem('carts', JSON.stringify(cartsInStore));
                addItemToCart(payload);
            }
        }
    };
  };

  const mergeUserOrdersAndLocalStorage = async () => {
    if (authStore.userData) {
        try {
            const response = await axios.get('carts/mine/products');
            const itemsFromDB = response.data;
            const newItemsFromDB = [];
            itemsFromDB.forEach( async dbItem => {
                const isCommonItem = orders.value.filter( siteItem => siteItem.product.id === dbItem.product.id);
                if (isCommonItem.length) {
                    const newAmount = isCommonItem[0].amount + dbItem.amount;
                    await updateItemInDB({ amount: newAmount, product: dbItem.product });
                    const storage = JSON.parse(localStorage.getItem('carts'));
                    const otherItemsInStor = storage.filter(item => item.product.id !== isCommonItem[0].product.id);
                    localStorage.setItem('carts', JSON.stringify(otherItemsInStor))
                } else {
                    newItemsFromDB.push({ amount: dbItem.amount, product: dbItem.product});
                }
            });
            // console.log(newItemsFromDB);
            newItemsFromDB.forEach( async newItem => {
                updateItemInCart({ amount: newItem.amount , product: newItem.product });
            });
            const newItemsFromSite = JSON.parse(localStorage.getItem('carts'));
            if (newItemsFromSite.length) {
                newItemsFromSite.forEach( async newItem => {
                    await addItemToDB(newItem);
                    const storage = JSON.parse(localStorage.getItem('carts'));
                    const otherItemsInStor = storage.filter(item => item.product.id !== newItem.product.id);
                    localStorage.setItem('carts', JSON.stringify([ ...otherItemsInStor ]));
                })
            }  
        } catch (e) {
          console.log(e);
            // notificationsStore.addMessage({name: "Не возможно обновить в корзине" + e, icon: "error", id: '1'});
        }
    }
  };

  const deleteItemsFromDB = async ( itemData ) => {
    if (authStore.userData) {
        try {
            await axios.delete('carts/mine/products/' + itemData.product.id);
            removeItemFromCart({amount : itemData.amount, product: itemData.product});
        } catch (e) {
            console.log(e);
            // notificationsStore.addMessage({name: "Не возможно обновить в корзине" + e, icon: "error", id: '1'});
        }
    }
  };

  const updateItemInDB = async (itemData) => {
    if (authStore.userData) {
        try {
            const response = await axios.patch('carts/mine/products/' + itemData.product.id, itemData);
            updateItemInCart({ amount : response.data.amount, product: itemData.product });
        } catch (e) {
            console.log(e);
            // notificationsStore.addMessage({name: "Не возможно обновить в корзине" + e, icon: "error", id: '1'});
        }
    }
  };

  const addItemToDB = async (itemData) => {
    if (authStore.userData) {
        try {
            const response = await axios.post('carts/mine/products', { product_id: itemData.product.id, amount: itemData.amount });
            updateItemInCart({ amount : response.data.amount, product: itemData.product });
        } catch (e) {
            console.log(e);
            // notificationsStore.addMessage({name: "Не возможно обновить в корзине" + itemData.product.name, icon: "error", id: '1'});
        }
    }
  };

  const addItemToCart = (item) => {
    const isItemInCart = orders.value.filter(element => element.product.id === item.product.id);
    if (isItemInCart.length) {
      isItemInCart[0].amount = isItemInCart[0].amount + item.amount;
    } else {
      orders.value.push(item);
    }
  };

  const updateItemInCart = (item) => {
    const isItemInCart = orders.value.filter(element => element.product.id === item.product.id);
    if (isItemInCart.length) {
      isItemInCart[0].amount = item.amount;
    } else {
      orders.value.push(item);
    }
  };

  const removeItemFromCart = (item) => {
    const filteredItemsInCart = orders.value.filter(element => element.product.id !== item.product.id);
    orders.value = [...filteredItemsInCart];
  };

  const sendOrderRequest = async (itemData) => {
    // if (rootGetters['auth/USER']) {
        try {
            const response = await axios.post('orders', itemData);
            // commit("UPDATE_ITEM_IN_CART", { amount : response.data.amount, product: itemData.product });
            orders.value.forEach(async item => {
              await deleteItemsFromDB(item);
              removeItemFromCart(item);
            })
            // commit("SET_ORDERS", []);
            setIsApplicationOpen(false);
            profileStore.changeScreen(0);
            headerStore.setPopUpAction('ShowCompleteMsg');
            const msg ={};
            msg.main = 'Наш менеджер свяжется с вами в ближайшее время.';
            msg.bolt = 'Время работы:';
            msg.sub = ' Пн-Пт - 9:00 - 17:00'
            headerStore.setPopUpMessage(msg);
            headerStore.setIsPopUpOpen(true);
        } catch (e) {
            console.log(e);
            // notificationsStore.addMessage({name: "Не возможно отправить заказ", icon: "error", id: '1'});
        }
    // }
  };

  const getOrdersDocuments = async () => {
    try {
      const response = await axios.get('orders/mine');
      const sorted = response.data.sort((a,b) => {
        return (Number(b.id) - Number(a.id))
      });
      orderDocuments.value = sorted;
    } catch (e) {
      console.log(e);
      // notificationsStore.addMessage({name: "Не возможно обновить заказы" + e, icon: "error", id: '1'});
    }
  };

  const clearOrderDocuments = () => {
   orderDocuments.value = [];
  };


  return {
    orders,
    orderDocuments,
    deliveryTypes,
    isApplicationOpen,
    totalOrderCost,
    totalOrderQuantity,
    getOrderDeliveryTypes,
    setIsApplicationOpen,
    clearOrders,
    getUserOrder,
    updateItemsInCart,
    mergeUserOrdersAndLocalStorage,
    sendOrderRequest,
    getOrdersDocuments,
    clearOrderDocuments,
  }
});

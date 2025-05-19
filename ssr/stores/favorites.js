import axios from "@/utils/api";
import { ref } from 'vue';
import { defineStore } from 'pinia';
import { useNotificationsStore } from "@/stores/notifications";
import { useAuthStore } from "@/stores/auth";

export const useFavoritesStore = defineStore ('favoritesStore', () => {

  const notificationsStore = useNotificationsStore();
  const authStore = useAuthStore();

  const favorites = ref([]);
  const fullFavorites = ref([]);

  const clearFullFavorites = () => {
    fullFavorites.value = [];
  };

  const clearFavorites = () => {
    favorites.value = [];
  };

  const addItemToFavorite = (payload) => {
    const isItemInFavorite = favorites.value.filter(item => item.product.id === payload.product.id);
    if (!isItemInFavorite.length) {
        favorites.value.push(payload);
    }
  };

  const removeItemFromFavorite = (payload) => {
    const filteredItemsInFavorite = favorites.value.filter(item => item.product.id !== payload.product.id);
    favorites.value = [...filteredItemsInFavorite];
  };

  const addFavoriteToDB = async (itemData) => {
    if (authStore.userData) {
        try {
            await axios.post('watch_lists/mine/products', { product_id: itemData.product.id });
            addItemToFavorite({ product: itemData.product });
        } catch (e) {
            console.log(e);
            // notificationsStore.addMessage({name: "Не возможно обновить в корзине", icon: "error", id: '1'});
        }
    }
  };

  const getUserFavorite = async () => {
    if (localStorage.getItem("authToken")) {
      try {
        const response = await axios.get('watch_lists/mine/products');
        favorites.value = response.data;
      } catch (e) {
        console.log(e);
        // notificationsStore.addMessage({name: "Не возможно обновить избранное", icon: "error", id: '1'});
      }
    } else {
      const isFavoritesInStore = localStorage.getItem('favorites');
      const favoritesInStore = isFavoritesInStore ? JSON.parse(isFavoritesInStore) : [];
      favorites.value = favoritesInStore;
    }
  };

  const updateIsWishInCart = async (payload) => {
    const type = payload.type; 
    const itemData = JSON.parse(JSON.stringify(payload.itemData));
    const product = itemData.product;
    if (authStore.userData) {
      // обновим базу
      if (type === 'set') {
        const isPresentFavoriteInStore = favorites.value.filter(item => item.product.id === product.id);
        if (!isPresentFavoriteInStore.length) {
          await addFavoriteToDB({ product });
        }
      } else if (type === 'remove') {
        const isPresentFavoriteInStore = favorites.value.filter(item => item.product.id === product.id);
        if (isPresentFavoriteInStore.length) {
          await deleteFavoriteFromDB({ product });
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
            addItemToFavorite({ product });
          }
        } else if (type === 'remove') {
          const isPresentFavoriteInStore = favoritesInStore.filter(item => item.product.id === product.id);
          if (isPresentFavoriteInStore.length) {
            const otherFavorites = favoritesInStore.filter(item => item.product.id !== product.id);
            localStorage.setItem('favorites', JSON.stringify([...otherFavorites]));
            removeItemFromFavorite(itemData);
          }
        }             
    }
  };

  const mergeUserFavoritesAndLocalStorage = async () => {
    if (authStore.userData) {
      try {
          const response = await axios.get('watch_lists/mine/products');
          const itemsFromDB = response.data;
          const newItemsFromDB = [];
          itemsFromDB.forEach( dbItem => {
            const isCommonItem = favorites.value.filter( siteItem => siteItem.product.id === dbItem.product.id);
            if (isCommonItem.length) {
              const storage = JSON.parse(localStorage.getItem('favorites'));
              const otherItemsInStor = storage.filter(item => item.product.id !== isCommonItem[0].product.id);
              localStorage.setItem('favorites', JSON.stringify(otherItemsInStor))
            } else {
              newItemsFromDB.push({ product: dbItem.product});
            }
          });
          newItemsFromDB.forEach( newItem => {
            addItemToFavorite({ product: newItem.product });
          });
          const newItemsFromSite = JSON.parse(localStorage.getItem('favorites'));
          if (newItemsFromSite.length) {
            newItemsFromSite.forEach( async newItem => {
              await addFavoriteToDB(newItem);
              const storage = JSON.parse(localStorage.getItem('favorites'));
              const otherItemsInStor = storage.filter(item => item.product.id !== newItem.product.id);
              localStorage.setItem('favorites', JSON.stringify([ ...otherItemsInStor ]));
            })
          }  
      } catch (e) {
        console.log(e);
        // notificationsStore.addMessage({name: "Не возможно обновить корзину", icon: "error", id: '1'});
      }
    }
  };

  const deleteFavoriteFromDB = async (itemData) => {
    if (authStore.userData) {
      try {
        await axios.delete('watch_lists/mine/products/' + itemData.product.id);
        removeItemFromFavorite({ product: itemData.product});
      } catch (e) {
        console.log(e);
        // notificationsStore.addMessage({name: "Не возможно обновить в корзине", icon: "error", id: '1'});
      }
    }
  };

  const getUserFullFavorite = async () => {
    favorites.value.forEach( async item => {
      try {
        const response = await axios.get('products/' + item.product.id);
        fullFavorites.value.push(response.data);
      } catch (e) {
        console.log(e);
        // notificationsStore.addMessage({name: "Не возможно обновить избранное", icon: "error", id: '1'});
      }  
    }); 
  };

  return {
    favorites,
    fullFavorites,
    clearFullFavorites,
    clearFavorites,
    getUserFavorite,
    updateIsWishInCart,
    mergeUserFavoritesAndLocalStorage,
    getUserFullFavorite,
  }
});

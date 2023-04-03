import { IDeliveryType } from "../types";

const state = {
  user: {},
  errors: {},
  isLoading: false,
  deliveryTypesData: [] as Array<IDeliveryType>,
  articles: [] as Array<IDeliveryType>,
  banners: [] as Array<IDeliveryType>,
  partners: [] as Array<IDeliveryType>,
  callRequests: [] as Array<IDeliveryType>,
  feedbackRequests: [] as Array<IDeliveryType>,
  orders: [] as Array<IDeliveryType>,
  orderTypes: [
    {id: 'P', name: 'В обработке'},
    {id: 'S', name: 'Отправлен'},
    {id: 'c', name: 'Отменен'},
    {id: 'C', name: 'Выполнен'},
    {id: '', name: 'Все заказы'},
  ],
  isPopUpOpen: false, 
  categories: [] as Array<IDeliveryType>,
  activeCategory: '' as string,
  settings: {} as IDeliveryType,
  stocks: [] as Array<IDeliveryType>,
  goods: [] as Array<IDeliveryType>,
}

export type State = typeof state
export { state }

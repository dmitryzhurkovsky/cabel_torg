import { IDeliveryType } from "../types";

const state = {
  user: {},
  errors: {},
  isLoading: false,
  deliveryTypesData: [] as Array<IDeliveryType>,
  articles: [] as Array<IDeliveryType>,
  partners: [] as Array<IDeliveryType>,
  callRequests: [] as Array<IDeliveryType>,
  feedbackRequests: [] as Array<IDeliveryType>,
}

export type State = typeof state
export { state }

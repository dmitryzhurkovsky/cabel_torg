import { IDeliveryType } from "../types";

const state = {
  user: {},
  errors: {},
  isLoading: false,
  deliveryTypesData: [] as Array<IDeliveryType>
}

export type State = typeof state
export { state }

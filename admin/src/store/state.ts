import { IdeliveryType } from "../types";

const state = {
  user: {},
  errors: {},
  isLoading: false,
  deliveryTypesData: [] as Array<IdeliveryType>
}

export type State = typeof state
export { state }

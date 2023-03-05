import { type } from "os"

interface IDeliveryType {
  [key: string]: any
}

type ITableHeadItem = {
  db: string,
  name: string,
  type: string,
  src: string,
}

type ITableHead = Array<ITableHeadItem>

export type { 
  IDeliveryType, 
  ITableHead, 
  ITableHeadItem,
}
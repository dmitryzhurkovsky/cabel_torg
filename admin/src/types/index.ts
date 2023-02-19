interface IDeliveryType {
  [key: string]: string | number
}

type ITableHeadItem = {
  db: string,
  name: string
}

type ITableHead = Array<ITableHeadItem>

export type { 
  IDeliveryType, 
  ITableHead, 
  ITableHeadItem,
}
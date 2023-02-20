import { type } from "os"

interface IDeliveryType {
  [key: string]: string | number
}

type ITableHeadItem = {
  db: string,
  name: string
}

type ITableHead = Array<ITableHeadItem>

type IArticleItem = {
  [key: string]: string
}

type IArticles = Array<IArticleItem>

export type { 
  IDeliveryType, 
  ITableHead, 
  ITableHeadItem,
  IArticleItem,
  IArticles
}
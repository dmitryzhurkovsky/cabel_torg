<template>
    <div v-it="cartItemData && quantity !==0">
        <a class="product__img" href="">
            <img v-if = "cartItemData.images" :src=getImagePath(cartItemData.images) alt="">
            <img v-if = "!cartItemData.images" src="../../assets/no_image.jpg" alt="">
        </a>
        <div class="product__info">
            <div class="product__article  _label mb-20">Артикул: <span>{{ cartItemData.vendor_code }}</span></div>
            <a  class="product__title" href="">Вилка RJ-45 cat 5E FTP для витой пары 8P8C (100 шт) экранированная</a>
            <div class="icon__row mt-20">
                <span class="icon icon-favorite">В избранное</span>
                <span class="icon icon-delete" @click="onOperationWithCartItem(cartItemData, 'remove')">Удалить</span>
            </div>
        </div>
        <div class="product__count flex-center">
            <div class="_label mb-20">Количество:</div>
            <div class="flex-center">
                <span class="icon-minus" @click="onOperationWithCartItem(cartItemData, 'decrease')"></span>
                <input class="product__input" type="text" v-model="quantity"  @input="onOperationWithCartItem(cartItemData, 'set')">
                <span class="icon-plus" @click="onOperationWithCartItem(cartItemData, 'increase')"></span>
            </div>
        </div>

        <div class="product__price">
            <div class="_label mb-20">Стоимость (с учетом НДС):</div>
            <div class="old_price">
                <span>70</span>BYN
                <span>/{{ cartItemData?.base_unit?.full_name }}</span>
            </div>
            <div class="current_price">
                <span>{{ cartItemData.price }}</span> BYN
            </div>
        </div>
    </div>
    
</template>

<script>
  import axios from "axios";
  import {mapActions, mapMutations} from 'vuex'

  export default {
    name: 'CartItem',
  
    props: {
        cartItem: null,
    },

    data(){
        return {
            cartItemData: {},
            quantity: 0,
        }
    },

    async mounted(){
        try {
            const response = await axios.get(process.env.VUE_APP_API_URL + 'products/' + this.cartItem.product.id);
            this.cartItemData = response.data;
            this.quantity = this.cartItem.amount;
        } catch (e) {
            console.log(e);
            this.ADD_MESSAGE({name: "Не возможно загрузить рекомендованные товары ", icon: "error", id: '1'})
        }
    },

    methods:{
        ...mapMutations("notification", ["ADD_MESSAGE"]),
        ...mapActions("order", ["UPDATE_ITEMS_IN_CART"]),

        getImagePath(item) {
            let path = null;
            if (item) {
                const allPath = item.split(',');
                path = process.env.VUE_APP_IMAGES + allPath[0];
            }
            return path;
        },

        async onOperationWithCartItem(card, type) {
            if (type === 'decrease' && this.quantity === 1) {
                return;
            };
            const itemData = {
                amount: 0,
                product: {
                    id: card.id,
                    vendor_code: card.vendor_code,
                    name: card.name,
                    price: card.price,
                },
            };
            if (type === 'set') {
                itemData.amount = Number(this.quantity);
            }
            
            await this.UPDATE_ITEMS_IN_CART({itemData, type});
            if (type === 'increase') {
                this.quantity++;
            } else if (type === 'decrease') {
                this.quantity--;
            } 
        },

    }

  }
</script>

<style scoped lang="scss">
.product{

    &__img {
        width: 100%;
        flex-basis: 20%;
        img{
            max-width: 100%;
            object-fit: fill;
        }
    }
    &__info{

    .icon{
        font-size: 10px;
        line-height: 20px;
        color: #423E48;
        opacity: 0.6;
        &:before{
        margin-right: 5px;
        }
        &:nth-child(1){
        margin-right: 15px;
        }
        &:hover{
        opacity: 1;
        cursor: pointer;
        }
    }
    }

    &__article{

    }
    &__title{
        font-size: 14px;
        line-height: 24px;
        text-decoration-line: underline;
        color: #423E48;
    }
    &__status{

    }
    &__count{
        flex-direction: column;
        //margin: 24px 0;
        .icon-plus, .icon-minus{
            cursor: pointer;
        }
    }
    &__input{
        width: 40px;
        height: 40px;
        padding: 9px 8px;
        background: rgba(66, 62, 72, 0.07);
        border-radius: 2px;
        border: none;
        margin: 0 10px;
    }

    &__price{
        display: flex;
        flex-direction: column;
        align-items: flex-end;

        .old_price{
            font-size: 14px;
            line-height: 20px;
            text-decoration-line: line-through;
            opacity: 0.4;
            margin-bottom: 5px;
        }
        .current_price{
            font-size: 20px;
            line-height: 20px;
            color: #423E48;
            font-weight: 500;
        }

    }
}


</style>
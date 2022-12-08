

<script lang="ts" setup>
import { ElMessage } from 'element-plus'
import "../components/ShopItemView.vue"
const OnError = (text: string) => {
    ElMessage.error(text)
} 
</script>
<script lang="ts">
import type { ShopItem } from "../models/shop";
import { TryGetToken, GetToken } from "../global";
export default {
    data(): {
        loaded: boolean,
        allitems: Array<ShopItem>,
        cartitems: Array<ShopItem>
    } {
        return {
            loaded: false,
            cartitems: [],
            allitems: []
        }
    },
    methods: {
        RefreshAllItems: async function () {
            let items = await this.axios.post('getallitems', {
                token: GetToken()
            })
            this.allitems = items.data
            this.loaded = true;
        },
        RefreshCartItems: async function () {
            let items = await this.axios.post('getcartitems', {
                token: GetToken()
            })
            this.cartitems = items.data
            this.loaded = true;
        },
        AddToCart: async function (item: ShopItem) {
            let r = await this.axios.post('addtocart', {
                token: GetToken(),
                id: item.id,
                count: item.count
            })
            if (r.data.success) {
                this.RefreshCartItems()
            } else {
                OnError(r.data.message)
            }
        }
    },
    mounted() {
        let r = TryGetToken();
        if (!r.success) {
            this.$router.push("/login/goto")
            return
        }
        setTimeout(() => {
            this.RefreshAllItems()
            this.RefreshCartItems()
        }, 500);
    }
}
</script>
<template>
    <el-tabs>
        <el-tab-pane label="全部商品">
            <div>
                全部商品列表
                <table v-if="loaded">
                    <tr>
                        <th> 编号 </th>
                        <th> 商品名称 </th>
                        <th> 描述 </th>
                        <th> 操作 </th>
                    </tr>
                    <tr v-for="item in allitems">
                        <td>
                            {{ item.id }}
                        </td>
                        <td>
                            {{ item.name }}
                        </td>
                        <td>
                            {{ item.description }}
                        </td>
                        <td>
                            <shop-item-view :item="item" />
                        </td>
                        <td>
                            <el-button @click="AddToCart(item)">加入购物车</el-button>
                        </td>
                    </tr>
                </table>
                <div v-else>
                    正在获取商品列表
                </div>
                <el-button @click="RefreshAllItems">刷新列表</el-button>
            </div>
        </el-tab-pane>
        <el-tab-pane label="购物车">
            <div>
                购物车：
                <table v-if="loaded">
                    <tr>
                        <th> 编号 </th>
                        <th> 商品名称 </th>
                        <th> 描述 </th>
                        <th> 操作 </th>
                    </tr>
                    <tr v-for="item in cartitems">
                        <td> {{ item.id }} </td>
                        <td> {{ item.name }} </td>
                        <td> {{ item.description }} </td>
                        <td>
                            <shop-item-view :item="item" />
                        </td>
                    </tr>
                </table>
                <div v-else>
                    正在获取购物车商品
                </div>
                <el-button @click="RefreshCartItems">刷新购物车</el-button>
            </div>
        </el-tab-pane>
    </el-tabs>
</template> 
<style>
.btadd {
    margin-left: 5px;
}

.numtb {
    width: 30px
}
</style> 
<script lang="ts" >
class ShopItem {
    id: string = ""
    name: string = ""
    price: number = 0
    description: string = ""
    count: number = 1
}
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
    <div>
        <!--左侧-->
        <div class="left">
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
                        <button @click="item.count = (item.count ?? 0) + 1">
                            +
                        </button>
                        <input class="numtb" v-model="item.count">
                        <button v-bind:disabled="item.count <= 1" @click="item.count = (item.count ?? 2) - 1">
                            -
                        </button>
                        <button class="btadd">
                            移除
                        </button>
                    </td>-
                </tr>
            </table>
            <div v-else>
                正在获取购物车商品
            </div>
            <button @click="RefreshCartItems">刷新购物车</button>
        </div>
        <!-- 分割线 -->
        <div style="border:1px solid ;float:left;height:200px;"></div>
        <!--右侧-->
        <div class="right">
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
                        <button @click="item.count = (item.count ?? 0) + 1">
                            +
                        </button>
                        <input class="numtb" v-model="item.count">
                        <button v-bind:disabled="item.count <= 1" @click="item.count = (item.count ?? 2) - 1">
                            -
                        </button>
                        <button class="btadd">
                            添加
                        </button>
                    </td>
                </tr>
            </table>
            <div v-else>
                正在获取商品列表
            </div>
            <button @click="RefreshAllItems">刷新列表</button>
        </div>
    </div>
</template> 
<style>
.btadd {
    margin-left: 5px;
}

.numtb {
    width: 30px
}

.left {
    width: 50%;
    top: 20px;
}

.right {
    position: absolute;
    left: 50%;
    top: 20px;
}
</style>
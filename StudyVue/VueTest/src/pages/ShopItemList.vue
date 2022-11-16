<script lang="ts" >
import { TryGetToken, GetToken } from "../global";
export default {
    data(): {
        allitems: Array<{
            id: string,
            name: string,
            description: string
        }>
    } {
        return {
            allitems: []
        }
    },
    methods: {
        RefreshItems: async function () {
            let items = await this.axios.post('http://localhost:8080/getallitems', {
                token: GetToken()
            })
            this.allitems = items.data
        }
    },
    mounted() {
        let r = TryGetToken();
        if (!r.success) {
            window.location.href = "#/login/goto"
        }
        setTimeout(() => {

        }, 100);
    }
}
</script>
<template>
    <div>
        <h3>
            正在获取商品列表
        </h3>
    </div>
</template> 

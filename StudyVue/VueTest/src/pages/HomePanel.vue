<script lang="ts" >
import { TryGetToken } from "../global";
export default {
    data(): {
        token: undefined | string
    } {
        return {
            token: undefined
        }
    },
    methods: {

    },
    mounted() {
        let r = TryGetToken();
        if (!r.success) {
            window.location.href = "#/login/goto"
        } else {
            this.token = r.token;
        }
    }
}
</script>
<template>
    <div>
        <h3>
            主页
        </h3>
        会话ID：{{ token }}
    </div>
</template> 

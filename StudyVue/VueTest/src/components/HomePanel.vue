<script lang="ts" >
import { TryGetToken } from "../global";
export default {
    data() {
        return {
        }
    },
    methods: {

    },
    mounted() {
        let r = TryGetToken();
        if (!r.success) {
            window.location.href = "#/login/goto"
        }
    }
}
</script>
<template>
    <div class="greetings">
        <h3>
            主页
        </h3>
    </div>
</template> 

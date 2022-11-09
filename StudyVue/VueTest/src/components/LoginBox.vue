<script setup lang="ts">
defineProps<{
    msg: string
}>();
</script>
<script lang="ts" >
import axios from 'axios'
export default {
    data() {
        return {
            info: "test"
        }
    },
    methods: {
        Submit: async function () {
            alert(this.$data.info)
            let result = await axios.get("baidu.com")
            alert(result.data)
        }
    }
}
</script>
<template>
    <div class="greetings">
        <h1 class="green">{{ msg }}</h1>
        <h3>
            输入测试内容
        </h3>
        信息：
        <input v-model="info">
        <button v-on:click="Submit">
            提交
        </button>
    </div>
</template>
<style scoped>
h1 {
    font-weight: 500;
    font-size: 2.6rem;
    top: -10px;
}

h3 {
    font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
    text-align: center;
}

@media (min-width: 1024px) {

    .greetings h1,
    .greetings h3 {
        text-align: left;
    }
}
</style>

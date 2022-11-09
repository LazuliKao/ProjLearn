<script setup lang="ts">
defineProps<{
    msg: string
}>();
</script>
<script lang="ts" >
export default {
    data() {
        return {
            info: "test",
            result: ""
        }
    },
    methods: {
        Submit: async function () {
            let info = this.$data.info;
            let response = await this.axios.get("http://localhost:8080/add");
            let str: string = response.data
            this.$data.result = str;
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
        <h4>
            返回 {{ result }}
        </h4>
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

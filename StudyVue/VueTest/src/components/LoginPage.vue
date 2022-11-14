<script lang="ts" >
import { SetToken } from "../global";
export default {
    data() {
        return {
            user: "admin",
            result: "",
            success: false
        }
    },
    methods: {
        Submit: async function () {
            try {
                let user = this.$data.user;
                let response = await this.axios.post('http://localhost:8080/login', {
                    user: user,
                    passwordMd5: ''
                });
                const {
                    success,
                    message,
                    token
                }: {
                    success: boolean,
                    message: string,
                    token: string
                } = response.data
                this.success = success;
                if (success) {
                    this.result = message + "\n将在1秒后跳转";
                    setTimeout(() => {
                        location.href = "#/"
                        SetToken(token)
                    }, 1000);
                } else {
                    this.$data.result = "登录失败！\n信息：" + message;
                }
            } catch (error) {
                let err = (error as Error);
                this.$data.result = err.name + " : " + err.message;
            }
        }
    }
}
</script>
<template>
    <div class="greetings">
        <h1 class="green">输入信息以登录</h1>
        信息：
        <input v-model="user">
        <button v-on:click="Submit">
            登录
        </button>
        <h4>
            {{ result }}
            <a v-if="success" href="#/">主页</a>
        </h4>
    </div>
</template>
<style scoped>

</style>

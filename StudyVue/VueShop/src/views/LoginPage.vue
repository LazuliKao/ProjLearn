<script lang="ts" >
import { SetToken } from "../global";
export default {
    data() {
        return {
            user: "admin",
            password: "admin",
            result: "",
            success: false
        }
    },
    methods: {
        Submit: async function () {
            try {
                let response = await this.axios.post('http://localhost:8080/login', {
                    user: this.user,
                    passwordMd5: this.password
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
                        this.$router.push("/")
                        SetToken(token)
                    }, 1000);
                } else {
                    this.result = "登录失败！\n信息：" + message;
                }
            } catch (error) {
                let err = (error as Error);
                this.result = err.name + " : " + err.message;
            }
        }
    }
}
</script>
<template>
    <div class="main">
        帐号：<el-input v-model="user" placeholder="输入帐号" clearable />
        <br>
        密码：<el-input type="password" placeholder="输入密码" v-model="password" show-password clearable />
        <br>
        <h4>
            {{ result }}
            <a v-if="success" href="#/">主页</a>
        </h4>
        <el-button v-on:click="Submit" class="loginbutton">
            登录
        </el-button>
    </div>
</template>
<style scoped>
div.main {
    position: absolute;
    top: 20%;
    left: 50%;
    width:300px;
    transform: translate(-50%, -50%);
}

.loginbutton {
    position: absolute;
    margin-top: 10px;
}
</style>

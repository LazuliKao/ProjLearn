
<script setup lang="ts">
defineProps<{}>();
</script>
<script lang="ts" >
export default {
    data() {
        return {
            time: 3,
            timeoutids: new Array<number>()//当前计时器ID
        }
    },
    methods: {
        ClearTimeouts: function () {
            this.timeoutids.forEach(id => {
                clearTimeout(id)
            })
        }
    },
    mounted() {
        let i = 0;
        for (i = 0; i < this.time; i++) {
            this.timeoutids.push(
                setTimeout(() => {
                    this.time -= 1
                }, 1000 * i))
        }
        this.timeoutids.push(
            setTimeout(() => {
                window.location.href = "#/login"
            }, 1000 * i))
    },
}
</script>
<template>
    <div class="greetings">
        <h1 class="red">错误</h1>
        <h4>
            尚未登录！
            将在 {{ time }} 秒后跳转到
            <a href="#/login" :on-click="ClearTimeouts">登录界面</a>
        </h4>
    </div>
</template>
<style scoped>

</style>

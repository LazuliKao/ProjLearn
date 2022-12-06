<template>
    <el-input-number v-model="item.count" :min="1" :max="99" @change="handleChange" />
</template>
<script lang="ts" setup>
import type { ShopItem } from "../models/shop";
const props = defineProps<{
    item: ShopItem
}>()
const handleChange = (value: number) => {
    console.log(value)
    console.log(JSON.stringify(props.item))
}
</script>
<style>

</style>
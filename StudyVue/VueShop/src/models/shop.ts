export class ShopItem {
    id: string = ""
    name: string = ""
    price: number = 0
    description: string = ""
    count: number | undefined = undefined
    onCountChanged = () => {
        alert("count changed")
        console.log(JSON.stringify(this))
    }
}
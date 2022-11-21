let token: string | undefined = undefined
export function GetToken(): string {
    return token as string
}
export function TryGetToken(): { success: false } | { success: boolean, token: string } {
    if (token === undefined) {
        return {
            success: false
        }
    } else {
        return {
            success: true,
            token
        }
    }
}

export function SetToken(tk: string) {//设置当前连接密钥
    token = tk
}
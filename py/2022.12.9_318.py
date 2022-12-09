import re
def check_phone(phone_number):
    if re.match(r"^(\(\d{3}\)|\d{3}-)?\d{8}$", phone_number) != None:
        return True
    else:
        return False
def check_mail_code(mail_code):
    if re.match(r"^[1-9]\d{5}$", mail_code) != None:
        return True
    else:
        return False
def check_web_url(web_url):
    if re.match(r"^https?://\w+(?:\.[^\.]+)+(?:/.+)*$", web_url) != None:
        return True
    else:
        return False
phoneNumber = input("请输入手机号码：")
print(phoneNumber,"是有效的电话号码格式吗？", check_phone(phoneNumber))
mailCode = input("请输入邮政编码：")
print(mailCode,"是有效的邮政编码格式吗？", check_mail_code(mailCode))
webUrl = input("请输入网址：")
print(webUrl,"是有效的网址格式吗？",  check_web_url(webUrl))




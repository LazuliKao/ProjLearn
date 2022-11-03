# class NumberError(Exception):
#     def __init__(self, data) -> None:
#         Exception.__init__(self,data)
#         self.data=data
#     def __str__(self) -> str:
#         return self.data + ' 非法数值(<0)'
# def total(data):
#     total=0
#     for i in data:
#         if i < 0 :raise NumberError(str(i))
#         total+=i
#     return total
# # 测试代码
# data1 =(44,78,90,80,55)
# print("总计 = ",total(data1))
# data2=(44,78,90,-80,55)
# print("总计 = ",total(data2))

# import sys
# from unittest import result
# n = int(sys.argv[1])
# result = []
# factor = 2
# while factor**2 <= n:
#     while (n% factor) == 0:
#         n //= factor
#         result.append(factor)
#         print(n, factor)
#     factor += 1
# if n > 1:
#     result.append(n)
# print(result)

# for i in range(2, 100):
#     for x in range(2, i-1):
#         if i % x == 0:
#             break
#     else:
#         print(i)

# print([n for n in
#        filter(lambda i:
#               len([i % x for x in range(2, i-1) if i % x == 0]) == 0,
#               range(2, 100)
#               )
#        ])
output=print
info = []
for _ in range(5):
    id = input("id : ")
    name = input("name : ")
    grade= int(input("grade : "))
    info.append((id,name,grade))
for (id,name,grade) in info:
    output(id,name,grade)
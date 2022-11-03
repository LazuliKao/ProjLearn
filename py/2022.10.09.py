from PIL import Image
img=Image.open("C:\\Users\\LazuliKao\\Desktop\\aaa.png")
print(img.size)
img.resize((16,16)).save("C:\\Users\\LazuliKao\\Desktop\\aaa2.png")

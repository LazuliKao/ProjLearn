import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-length", default=-1, type=int, help="长度")
parser.add_argument("-width", default=-1, type=int, help="宽度")
args = parser.parse_args()
if args.width == -1:
    print("未指定width")
    exit()
if args.length == -1:
    print("未指定length")
    exit()
print(args)
area = args.width*args.length
c = 2*(args.width+args.length)
print("面积 = ", area)
print("周长 = ", c)

import math
l, w, h = map(int, input().split())
print(math.ceil((2*l*h + 2*w*h)/16))

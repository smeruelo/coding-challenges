dvorak = "bcdefghijklnopqrstuvwxyz.,;'-"
qwerty = "nihdyujgcvplsrxo;kf.,bt/ewzq'"
trans = str.maketrans(dvorak, qwerty)


for i in range(int(input())):
    decoded = input().translate(trans)
    print(f'Case #{i+1}: {decoded}')

products = []
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入價格： ')
    price = int(price)
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
print(products)

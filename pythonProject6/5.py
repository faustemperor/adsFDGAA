products = {}
for _ in range(3):
    product = input("Введите название продукта: ")
    price = float(input("Введите его стоимость: "))
    products[product] = price

wanted_product = input("Какой продукт вы хотите купить? ")
price = products.get(wanted_product)

if price is not None:
    print(f"Стоимость {wanted_product}: {price}")
else:
    print("Продукта нет в списке.")
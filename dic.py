from pprint import pprint

# product = {
#     "name": "iPhone 12 Pro",
#     "stock": 24,
#     "price": 65432.1,
    # "country": "RU"
# }

# print(product)

# print(len(product))

# product["memory"] = 64
# print(product)

# product["name"] = "iPhone 12 Pro"
# print(product)

# print(product["name"])

# print(product.get("qwe", 0))

# print(product.get("country", "CN"))

# print(product)
# del product["stock"]
# print(product)

# phones = ["iPhone 12 Pro", "Samsung Galaxy S21", "Xiaomi Mi11"]
# # pprint(product)
# product["recomended"] = phones
# pprint(product)
# pprint(product["recomended"])
# pprint(product["recomended"][0])
# product["recomended"].append("Iphone 9")
# pprint(product)

# stock = [
#     {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
#        'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
#     {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
#     {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
# ]
# pprint(stock[0]) #вывод словаря

# pprint(stock[0]["recomended"][0]) #вывод нулевого объекта списка

# stock[0]["recomended"].append("Xiaomi Mi11")
# stock[2]["price"] = stock[2]["price"] - 30000
# pprint(stock)

# print(type(stock))

# print(type(stock[0]))

# print(type(stock[0]["recomended"]))

cities = {"city": "Москва", "temperature": "20"}
print(cities["city"])

cities["temperature"] = int(cities["temperature"]) - 5
print(cities["temperature"])

pprint(cities)

print(cities.get("country", 0))

print(cities.get("country", "Russia"))

cities["date"] = "27.05.2019"
pprint(cities)

pprint(len(cities))


import json

def save_bill(input_file, output_file):
    with open(input_file) as f:
        data = json.load(f)

    with open(output_file, "w") as f:
        f.write(f"Чек клиента {data['customer_name']}\n")
        total_sum = 0
        for product in data["items"]:
            f.write(f"Товар {product['name']} Количество {product['quantity']} Цена {product['price']}\n")
            total_sum += product['quantity'] * product['price']
        f.write(f"Общая сумма чека: {total_sum}")

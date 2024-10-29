import json


def load_order_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_receipt(order_data):
    customer_name = order_data['customer_name']
    items = order_data['items']

    total_amount = sum(item['quantity'] * item['price'] for item in items)

    receipt_lines = [f'Имя клиента: {customer_name}\n']
    receipt_lines.append('Список товаров:\n')

    for item in items:
        receipt_lines.append(
            f"{item['name']} (количество: {item['quantity']}, цена за единицу: {item['price']} руб.)\n")

    receipt_lines.append(f'\nОбщая сумма заказа: {total_amount} руб.\n')

    return ''.join(receipt_lines)


def save_receipt(receipt, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(receipt)
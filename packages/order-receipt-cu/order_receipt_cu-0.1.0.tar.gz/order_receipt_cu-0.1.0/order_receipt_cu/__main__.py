import argparse
import json


def load_order(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        order_data = json.load(f)
    return order_data


def generate_receipt(order_data):
    customer_name = order_data['customer_name']
    items = order_data['items']

    total_sum = 0
    receipt_lines = [f"Имя клиента: {customer_name}\n", "Список товаров:\n"]

    for item in items:
        name = item['name']
        quantity = item['quantity']
        price = item['price']
        total_price = quantity * price
        total_sum += total_price
        receipt_lines.append(
            f"{name}, количество: {quantity}, цена за единицу: {price}, итоговая цена: {total_price}\n")

    receipt_lines.append(f"\nОбщая сумма заказа: {total_sum} руб.\n")
    return receipt_lines


def save_receipt(output_file, receipt_lines):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(receipt_lines)


def main():
    parser = argparse.ArgumentParser(description="Генерация чека по заказу")
    parser.add_argument('--input-file', type=str, required=True, help='Путь к входному JSON-файлу с данными заказа')
    parser.add_argument('--output-file', type=str, required=True, help='Путь к выходному текстовому файлу для чека')

    args = parser.parse_args()

    order_data = load_order(args.input_file)

    receipt_lines = generate_receipt(order_data)

    save_receipt(args.output_file, receipt_lines)


if __name__ == "__main__":
    main()
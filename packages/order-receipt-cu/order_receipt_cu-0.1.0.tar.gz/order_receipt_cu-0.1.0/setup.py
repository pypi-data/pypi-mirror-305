from setuptools import setup, find_packages

setup(
    name="order_receipt_cu",  # Название пакета
    version="0.1.0",  # Версия пакета
    description="Пакет для генерации чека на основе данных заказа",
    author="Egor",
    author_email="drobyazko_04@mail.ru",
    packages=find_packages(),  # Автоматический поиск всех пакетов
    install_requires=[],  # Список зависимостей (в данном случае пусто)
    entry_points={
        'console_scripts': [
            'order_receipt_cu=order_receipt_cu.__main__:main',  # Точка входа для запуска из консоли
        ],
    },
)
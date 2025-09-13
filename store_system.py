"""
Домашнее задание по курсу Python - ООП
ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: ПО для сети магазинов

Автор: Студент курса Zerocoder
Дата: 2025-09-13
"""


class Store:
    """
    Класс для представления магазина.
    
    Атрибуты:
        name (str): Название магазина
        address (str): Адрес магазина
        items (dict): Словарь товаров и их цен
    """
    
    def __init__(self, name, address):
        """
        Конструктор класса Store.
        
        Args:
            name (str): Название магазина
            address (str): Адрес магазина
        """
        self.name = name
        self.address = address
        self.items = {}  # Изначально ассортимент пустой

    def add_item(self, item_name, price):
        """
        Добавляет товар в ассортимент магазина.
        
        Args:
            item_name (str): Название товара
            price (float): Цена товара
        """
        self.items[item_name] = price
        print(f"В магазине '{self.name}' появился товар '{item_name}' по цене {price}.")

    def remove_item(self, item_name):
        """
        Удаляет товар из ассортимента магазина.
        
        Args:
            item_name (str): Название товара для удаления
        """
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """
        Получает цену товара по его названию.
        
        Args:
            item_name (str): Название товара
            
        Returns:
            float or None: Цена товара или None, если товар отсутствует
        """
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """
        Обновляет цену товара.
        
        Args:
            item_name (str): Название товара
            new_price (float): Новая цена товара
        """
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '{item_name}' обновлена. Новая цена: {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден для обновления цены.")

    def show_items(self):
        """Выводит весь ассортимент магазина."""
        print(f"\n--- Ассортимент магазина '{self.name}' ({self.address}) ---")
        if not self.items:
            print("Ассортимент пуст.")
        else:
            for item, price in self.items.items():
                print(f"- {item}: {price} руб.")


def demo_store_system():
    """Демонстрация работы системы магазинов."""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ СИСТЕМЫ МАГАЗИНОВ")
    print("=" * 50)
    
    # Создаем три разных магазина
    store1 = Store("Продукты у дома", "ул. Центральная, 1")
    store2 = Store("Книжный мир", "пр. Ленина, 45")
    store3 = Store("ТехноСила", "ул. Промышленная, 10")
    
    # Добавляем товары в каждый магазин
    print("\n--- Наполнение магазинов товарами ---")
    store1.add_item("Хлеб", 50)
    store1.add_item("Молоко", 80)
    store1.add_item("Яйца", 120)
    
    store2.add_item("Война и мир", 1200)
    store2.add_item("Мастер и Маргарита", 950)
    store2.add_item("Преступление и наказание", 800)
    
    store3.add_item("Смартфон", 25000)
    store3.add_item("Ноутбук", 70000)
    store3.add_item("Наушники", 5000)
    
    # Показываем ассортимент всех магазинов
    print("\n--- Ассортимент всех магазинов ---")
    store1.show_items()
    store2.show_items()
    store3.show_items()
    
    # Тестируем все методы на примере первого магазина
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ВСЕХ МЕТОДОВ НА МАГАЗИНЕ 'Продукты у дома'")
    print("=" * 60)
    
    # Показываем начальный ассортимент
    store1.show_items()
    
    # Добавляем новый товар
    print("\n--- Добавление нового товара ---")
    store1.add_item("Сыр", 250)
    store1.show_items()
    
    # Обновляем цену существующего товара
    print("\n--- Обновление цены товара ---")
    store1.update_price("Молоко", 85)
    store1.show_items()
    
    # Пытаемся обновить цену несуществующего товара
    print("\n--- Попытка обновить цену несуществующего товара ---")
    store1.update_price("Кефир", 90)
    
    # Удаляем товар
    print("\n--- Удаление товара ---")
    store1.remove_item("Хлеб")
    store1.show_items()
    
    # Пытаемся удалить несуществующий товар
    print("\n--- Попытка удалить несуществующий товар ---")
    store1.remove_item("Колбаса")
    
    # Запрашиваем цены товаров
    print("\n--- Запрос цен товаров ---")
    print(f"Цена на 'Сыр': {store1.get_price('Сыр')} руб.")
    print(f"Цена на 'Молоко': {store1.get_price('Молоко')} руб.")
    print(f"Цена на 'Колбаса' (отсутствует): {store1.get_price('Колбаса')}")


if __name__ == "__main__":
    """Запуск демонстрации при прямом вызове файла."""
    print("ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: ПО для сети магазинов")
    print("Автор: Студент курса Zerocoder")
    print()
    
    demo_store_system()
    
    print("\n" + "=" * 50)
    print("ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ ВЫПОЛНЕНО УСПЕШНО!")
    print("=" * 50)

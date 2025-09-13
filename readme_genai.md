### Задача 1: Менеджер задач

В этом задании нужно создать класс `Task`, который будет представлять одну задачу. У каждой задачи должны быть три **атрибута** (свойства): описание, срок и статус. [cite\_start]Также нужны **методы** (действия) для управления задачами. [cite: 280, 281, 282]

Для удобства мы создадим два класса:

1.  **`Task`**: будет описывать одну конкретную задачу (ее описание, срок, статус).
2.  **`TaskManager`**: будет управлять списком всех задач (добавлять новые, отмечать выполненные и показывать текущие).

Вот как будет выглядеть код:

```python
# Создаем класс Task, который является "шаблоном" для каждой отдельной задачи.
# У него есть атрибуты: описание, срок выполнения и статус.
class Task:
    # Метод __init__ - это конструктор. Он вызывается при создании нового объекта класса.
    # [cite_start]self - это ссылка на сам объект. [cite: 197, 199]
    def __init__(self, description, due_date):
        self.description = description  # Атрибут для хранения описания
        self.due_date = due_date        # Атрибут для срока выполнения
        self.is_done = False            # Статус по умолчанию "не выполнено"

    # Метод для отметки задачи как выполненной
    def mark_as_done(self):
        self.is_done = True
        print(f"Задача '{self.description}' отмечена как выполненная.")

    # Специальный метод для красивого отображения информации об объекте при печати
    def __str__(self):
        status = "Выполнено" if self.is_done else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"

# Создаем класс TaskManager для управления всеми задачами
class TaskManager:
    def __init__(self):
        self.tasks = []  # При создании менеджера создается пустой список для хранения задач

    # Метод для добавления новой задачи
    def add_task(self, description, due_date):
        [cite_start]new_task = Task(description, due_date) # Создаем объект (экземпляр) класса Task [cite: 79]
        self.tasks.append(new_task)
        print(f"Добавлена новая задача: '{description}'")

    # Метод для отметки задачи как выполненной по ее описанию
    def complete_task(self, description):
        found = False
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                found = True
                break
        if not found:
            print(f"Задача с описанием '{description}' не найдена.")

    # Метод для вывода списка только невыполненных задач
    def show_current_tasks(self):
        print("\n--- Список текущих (не выполненных) задач ---")
        current_tasks_exist = False
        for task in self.tasks:
            if not task.is_done:
                print(task)
                current_tasks_exist = True
        if not current_tasks_exist:
            print("Все задачи выполнены!")

# --- Пример использования ---

# Создаем объект класса TaskManager
my_manager = TaskManager()

# [cite_start]Добавляем задачи, вызывая метод add_task у нашего объекта [cite: 253]
my_manager.add_task("Подготовить отчет по Python", "20.09.2025")
my_manager.add_task("Сделать домашнее задание по ООП", "18.09.2025")
my_manager.add_task("Полить цветы", "17.09.2025")

# Показываем текущие задачи
my_manager.show_current_tasks()

# Отмечаем одну задачу как выполненную
my_manager.complete_task("Полить цветы")

# Снова показываем текущие задачи, чтобы увидеть изменения
my_manager.show_current_tasks()
```

-----

### \*Дополнительное задание: ПО для сети магазинов

[cite\_start]Здесь задача похожая: нужно создать класс `Store`, который будет шаблоном для создания разных магазинов. [cite: 284]

**План действий:**

1.  [cite\_start]Создадим класс `Store` с атрибутами `name`, `address` и `items`. [cite: 285]
2.  [cite\_start]Реализуем все требуемые методы: для добавления, удаления, обновления и получения цены товара. [cite: 287, 288, 289]
3.  [cite\_start]Создадим три разных объекта-магазина. [cite: 290]
4.  [cite\_start]Протестируем все методы на одном из магазинов. [cite: 291]

Вот код решения:

```python
# 1. Создание класса Store
class Store:
    # [cite_start]Конструктор для инициализации атрибутов магазина [cite: 303]
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Изначально ассортимент (словарь) пустой

    # [cite_start]Метод для добавления товара в ассортимент [cite: 288]
    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"В магазине '{self.name}' появился товар '{item_name}' по цене {price}.")

    # [cite_start]Метод для удаления товара [cite: 288]
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    # [cite_start]Метод для получения цены товара [cite: 289]
    def get_price(self, item_name):
        price = self.items.get(item_name) # .get() вернет None, если товара нет
        if price is not None:
            return price
        else:
            return None

    # [cite_start]Метод для обновления цены товара [cite: 289]
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар '{item_name}' обновлена. Новая цена: {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден для обновления цены.")
    
    # Метод для вывода ассортимента магазина
    def show_items(self):
        print(f"\n--- Ассортимент магазина '{self.name}' ({self.address}) ---")
        if not self.items:
            print("Ассортимент пуст.")
        else:
            for item, price in self.items.items():
                print(f"- {item}: {price} у.е.")

# 2. Создание нескольких объектов класса Store
store1 = Store("Продукты у дома", "ул. Центральная, 1")
store2 = Store("Книжный мир", "пр. Ленина, 45")
store3 = Store("ТехноСила", "ул. Промышленная, 10")

# Добавим товары в каждый магазин
store1.add_item("Хлеб", 50)
store1.add_item("Молоко", 80)

store2.add_item("Война и мир", 1200)
store2.add_item("Мастер и Маргарита", 950)

store3.add_item("Смартфон", 25000)
store3.add_item("Ноутбук", 70000)


# 3. Тестирование методов на примере магазина "Продукты у дома"
print("\n" + "="*20)
print("Тестирование методов магазина 'Продукты у дома'")
print("="*20)

# Показываем начальный ассортимент
store1.show_items()

# Добавляем новый товар
store1.add_item("Сыр", 250)
store1.show_items()

# Обновляем цену существующего товара
store1.update_price("Молоко", 85)
store1.show_items()

# Пытаемся обновить цену несуществующего товара
store1.update_price("Кефир", 90)

# Удаляем товар
store1.remove_item("Хлеб")
store1.show_items()

# Запрашиваем цену существующего и отсутствующего товаров
print(f"\nЦена на 'Сыр': {store1.get_price('Сыр')}")
print(f"Цена на 'Колбаса': {store1.get_price('Колбаса')}")
```
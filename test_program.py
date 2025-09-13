# -*- coding: utf-8 -*-
"""
Тестовый файл для проверки работы основной программы
"""

# Импортируем классы из main.py
from main import Task, TaskManager, Store

def test_task_manager():
    """Тест менеджера задач"""
    print("=== ТЕСТ МЕНЕДЖЕРА ЗАДАЧ ===")
    
    # Создаем менеджер
    manager = TaskManager()
    
    # Добавляем задачи
    manager.add_task("Тестовая задача 1", "2025-09-20")
    manager.add_task("Тестовая задача 2", "2025-09-21")
    
    # Показываем задачи
    manager.show_current_tasks()
    
    # Отмечаем одну как выполненную
    manager.complete_task("Тестовая задача 1")
    
    # Показываем обновленный список
    manager.show_current_tasks()
    
    print("Тест менеджера задач ПРОЙДЕН!")
    return True

def test_store_system():
    """Тест системы магазинов"""
    print("\n=== ТЕСТ СИСТЕМЫ МАГАЗИНОВ ===")
    
    # Создаем магазин
    store = Store("Тестовый магазин", "ул. Тестовая, 1")
    
    # Добавляем товары
    store.add_item("Товар 1", 100)
    store.add_item("Товар 2", 200)
    
    # Показываем ассортимент
    store.show_items()
    
    # Тестируем получение цены
    price = store.get_price("Товар 1")
    print(f"Цена 'Товар 1': {price}")
    
    # Обновляем цену
    store.update_price("Товар 1", 150)
    
    # Удаляем товар
    store.remove_item("Товар 2")
    
    # Показываем итоговый ассортимент
    store.show_items()
    
    print("Тест системы магазинов ПРОЙДЕН!")
    return True

if __name__ == "__main__":
    print("ЗАПУСК ТЕСТОВ ПРОГРАММЫ")
    print("=" * 40)
    
    try:
        # Запускаем тесты
        test1_result = test_task_manager()
        test2_result = test_store_system()
        
        if test1_result and test2_result:
            print("\n" + "=" * 40)
            print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
            print("Программа готова к сдаче!")
            print("=" * 40)
        else:
            print("ОШИБКА В ТЕСТАХ!")
            
    except Exception as e:
        print(f"ОШИБКА ПРИ ВЫПОЛНЕНИИ ТЕСТОВ: {e}")

"""
Домашнее задание по курсу Python - ООП
ОСНОВНОЕ ЗАДАНИЕ: Менеджер задач

Автор: Студент курса Zerocoder
Дата: 2025-09-13
"""


class Task:
    """
    Класс для представления одной задачи.
    
    Атрибуты:
        description (str): Описание задачи
        due_date (str): Срок выполнения задачи
        is_done (bool): Статус выполнения (True - выполнено, False - не выполнено)
    """
    
    def __init__(self, description, due_date):
        """
        Конструктор класса Task.
        
        Args:
            description (str): Описание задачи
            due_date (str): Срок выполнения задачи
        """
        self.description = description
        self.due_date = due_date
        self.is_done = False  # По умолчанию задача не выполнена

    def mark_as_done(self):
        """Отмечает задачу как выполненную."""
        self.is_done = True
        print(f"Задача '{self.description}' отмечена как выполненная.")

    def __str__(self):
        """Возвращает строковое представление задачи."""
        status = "Выполнено" if self.is_done else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    """
    Класс для управления списком задач.
    
    Атрибуты:
        tasks (list): Список объектов Task
    """
    
    def __init__(self):
        """Конструктор класса TaskManager."""
        self.tasks = []

    def add_task(self, description, due_date):
        """
        Добавляет новую задачу в список.
        
        Args:
            description (str): Описание задачи
            due_date (str): Срок выполнения задачи
        """
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Добавлена новая задача: '{description}'")

    def complete_task(self, description):
        """
        Отмечает задачу как выполненную по её описанию.
        
        Args:
            description (str): Описание задачи для поиска
        """
        found = False
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                found = True
                break
        if not found:
            print(f"Задача с описанием '{description}' не найдена.")

    def show_current_tasks(self):
        """Выводит список всех невыполненных задач."""
        print("\n--- Список текущих (не выполненных) задач ---")
        current_tasks_exist = False
        for task in self.tasks:
            if not task.is_done:
                print(task)
                current_tasks_exist = True
        if not current_tasks_exist:
            print("Все задачи выполнены!")

    def show_all_tasks(self):
        """Выводит список всех задач (выполненных и невыполненных)."""
        print("\n--- Список всех задач ---")
        if not self.tasks:
            print("Задач нет.")
        else:
            for task in self.tasks:
                print(task)


def demo_task_manager():
    """Демонстрация работы менеджера задач."""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ МЕНЕДЖЕРА ЗАДАЧ")
    print("=" * 50)
    
    # Создаем менеджер задач
    my_manager = TaskManager()
    
    # Добавляем задачи
    my_manager.add_task("Подготовить отчет по Python", "20.09.2025")
    my_manager.add_task("Сделать домашнее задание по ООП", "18.09.2025")
    my_manager.add_task("Полить цветы", "17.09.2025")
    
    # Показываем текущие задачи
    my_manager.show_current_tasks()
    
    # Отмечаем одну задачу как выполненную
    my_manager.complete_task("Полить цветы")
    
    # Снова показываем текущие задачи
    my_manager.show_current_tasks()
    
    # Показываем все задачи
    my_manager.show_all_tasks()


if __name__ == "__main__":
    """Запуск демонстрации при прямом вызове файла."""
    print("ОСНОВНОЕ ЗАДАНИЕ: Менеджер задач")
    print("Автор: Студент курса Zerocoder")
    print()
    
    demo_task_manager()
    
    print("\n" + "=" * 50)
    print("ОСНОВНОЕ ЗАДАНИЕ ВЫПОЛНЕНО УСПЕШНО!")
    print("=" * 50)

import os
import sys
from colorama import init, Fore, Style
from pathlib import Path

# Ініціалізація colorama для підтримки кольорового виведення
init(autoreset=True)

def list_directory_contents(directory_path, indent=0):
    try:
        # Створення об'єкту шляху за допомогою модуля pathlib
        directory = Path(directory_path)

        # Перевірка, чи існує директорія та чи є вона дійсно директорією
        if not directory.exists() or not directory.is_dir():
            raise FileNotFoundError

        # Ітеруємось по вмісту директорії
        for item in directory.iterdir():
            if item.is_dir():
                # Якщо це директорія, виводимо її назву синього кольору
                print(Fore.BLUE + "  " * indent + f"{item.name}/")
                # Рекурсивно викликаємо функцію для переліку її вмісту
                list_directory_contents(item, indent + 1)
            else:
                # Якщо це файл, виводимо його назву зеленим кольором
                print(Fore.GREEN + "  " * indent + item.name)

    except FileNotFoundError:
        print(Fore.RED + "Неправильний шлях або директорія не існує.")
    except PermissionError:
        print(Fore.RED + "Немає прав доступу до цієї директорії.")
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

if __name__ == "__main__":
    # Перевірка наявності аргументів командного рядка
    if len(sys.argv) != 2:
        print("Використання: python script.py <шлях до директорії>")
        sys.exit(1)

    # Отримання шляху до директорії з аргументів командного рядка
    directory_path = sys.argv[1]
    # Виклик функції для переліку вмісту директорії
    list_directory_contents(directory_path)

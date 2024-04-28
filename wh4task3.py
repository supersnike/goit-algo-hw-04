import os
import sys
from colorama import init, Fore, Style
from pathlib import Path

# Ініціалізація colorama для підтримки кольорового виведення
init(autoreset=True)

def list_directory_contents(directory_path, indent=0):
    try:
        directory = Path(directory_path)

        if not directory.exists() or not directory.is_dir():
            raise FileNotFoundError

        for item in directory.iterdir():
            if item.is_dir():
                print(Fore.BLUE + "  " * indent + f"{item.name}/")
                list_directory_contents(item, indent + 1)
            else:
                print(Fore.GREEN + "  " * indent + item.name)

    except FileNotFoundError:
        print(Fore.RED + "Неправильний шлях або директорія не існує.")
    except PermissionError:
        print(Fore.RED + "Немає прав доступу до цієї директорії.")
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python script.py <шлях до директорії>")
        sys.exit(1)

    directory_path = sys.argv[1]
    list_directory_contents(directory_path)

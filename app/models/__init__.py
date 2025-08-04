import os
import importlib

# Получаем путь к текущей папке models/
models_dir = os.path.dirname(__file__)
module_name = __name__  # → "src.models"

# Импортируем каждый .py-файл, кроме __init__.py
for filename in os.listdir(models_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        import_path = f"{module_name}.{filename[:-3]}"  # "src.models.user"
        importlib.import_module(import_path)
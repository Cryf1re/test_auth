import os
import importlib

models_dir = os.path.dirname(__file__)
module_name = __name__  # → "app.models"

for filename in os.listdir(models_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        import_path = f"{module_name}.{filename[:-3]}"
        importlib.import_module(import_path)
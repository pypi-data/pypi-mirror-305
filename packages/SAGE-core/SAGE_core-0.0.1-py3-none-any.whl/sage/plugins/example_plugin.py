# plugins/example_plugin.py

class Plugin:
    def __init__(self, core):
        self.core = core
        self.core.register_api("example_api", self.example_api_method)  # Регистрация API
        self.core.register_hook("startup", self.on_startup)  # Регистрация хука

    def example_api_method(self, data):
        print(f"API метод example_api вызван с данными: {data}")

    def on_startup(self):
        print("Example Plugin: событие startup выполнено.")

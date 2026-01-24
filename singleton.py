class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.settings = {}
            self.initialized = True
    def set(self, key, value):
        self.settings[key] = value
    def get(self, key, default=None):
        return self.settings.get(key, default)
# Example usage:
config1 = Config()
config1.set('theme', 'dark')
config2 = Config()
print(config2.get('theme'))  # Output: dark
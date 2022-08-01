class Singleton(type):
    """Класс в метаклассы для синглтонов."""
    _instances = {}

    def call(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

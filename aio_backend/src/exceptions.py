class AuthenticationError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


class RepositoryError(Exception):
    """Базовый класс для ошибок репозитория"""


class ObjectNotFound(RepositoryError):
    """Объект не найден в репозитории"""

from abc import ABC, abstractmethod

from src.dto.posts import PostDTO, PostCreateDTO
from src.dto.users import UserDTO


class AbstractPostRepository(ABC):

    @abstractmethod
    async def get(self, post_id: int) -> PostDTO: ...

    @abstractmethod
    async def create(self, instance: PostCreateDTO) -> PostDTO: ...

    @abstractmethod
    async def get_list(self, search: str = "") -> list[PostDTO]: ...

    @abstractmethod
    async def update(self, instance: PostDTO) -> PostDTO: ...

    @abstractmethod
    async def delete(self, post_id: int) -> None: ...

    @abstractmethod
    async def list_by_author(self, author_id: int) -> list[PostDTO]: ...


class AbstractUserRepository(ABC):

    @abstractmethod
    async def get(self, user_id: int) -> UserDTO: ...

    @abstractmethod
    async def get_by_username(self, username: str) -> UserDTO: ...

    @abstractmethod
    async def create(self, instance: UserDTO) -> UserDTO: ...

    @abstractmethod
    async def update(self, instance: UserDTO) -> UserDTO: ...

from abc import ABC, abstractmethod

from src.dto.posts import PostCreateDTO, PostDTO
from src.dto.users import UserDTO


class AbstractPostRepository(ABC):

    @abstractmethod
    async def get(self, post_id: int) -> PostDTO:
        """
        Возвращает пост по id

        Args:
            post_id (int): id поста
        Raises:
            ObjectNotFound: если пост не найден.
        """

    @abstractmethod
    async def create(self, instance: PostCreateDTO) -> PostDTO: ...

    @abstractmethod
    async def get_list(
        self, page: int, page_size: int, search: str = "", author_username: str = ""
    ) -> tuple[list[PostDTO], int]: ...

    @abstractmethod
    async def update(self, instance: PostDTO) -> PostDTO: ...

    @abstractmethod
    async def delete(self, post_id: int) -> None: ...


class AbstractUserRepository(ABC):

    @abstractmethod
    async def get(self, user_id: int) -> UserDTO: ...

    @abstractmethod
    async def get_by_username(self, username: str) -> UserDTO: ...

    @abstractmethod
    async def create(self, instance: UserDTO) -> UserDTO: ...

    @abstractmethod
    async def update(self, instance: UserDTO) -> UserDTO: ...

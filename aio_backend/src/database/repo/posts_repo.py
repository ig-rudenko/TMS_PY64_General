from sqlalchemy import delete, or_, select, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import PostModel, UserModel
from src.dto.posts import PostCreateDTO, PostDTO
from src.exceptions import ObjectNotFound
from src.repository.abstract import AbstractPostRepository


class SqlAlchemyPostRepository(AbstractPostRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, post_id: int) -> PostDTO:
        query = select(PostModel).where(PostModel.id == post_id)
        result = await self.session.execute(query)
        post = result.scalar_one_or_none()
        if post is None:
            raise ObjectNotFound(f"Post with id {post_id} not found")
        return self._to_dto(post)

    async def create(self, instance: PostCreateDTO) -> PostDTO:
        post = PostModel(
            title=instance.title,
            content=instance.content,
            user_id=instance.author_id,
        )
        print("Добавляем объект в сессию (add):")
        self.session.add(post)  # Добавляем объект в сессию.
        print("Отправляем изменения в БД (flush):")
        await self.session.flush()  # Передаём изменения в БД для текущей сессии.
        print("Обновляем объект (refresh):")
        await self.session.refresh(post)  # Обновляем объект, чтобы получить id.
        return self._to_dto(post)

    async def get_list(
        self, page: int, page_size: int, search: str = "", author_username: str = ""
    ) -> tuple[list[PostDTO], int]:
        offset = (page - 1) * page_size
        query = (
            select(func.count(), PostModel)
            .order_by(PostModel.created_at.desc())
            .limit(page_size)
            .offset(offset)
        )

        if search:
            query = query.where(
                or_(
                    PostModel.title.icontains(search),
                    PostModel.content.icontains(search),
                )
            )
        if author_username:
            query = query.join(UserModel, UserModel.id == PostModel.user_id).where(
                UserModel.username == author_username
            )

        result = await self.session.execute(query)

        posts = []
        total_count = 0
        for count, post in result:
            if not total_count:
                total_count = count
            posts.append(self._to_dto(post))

        return posts, count

    async def update(self, instance: PostDTO) -> PostDTO:
        query = (
            update(PostModel)
            .where(PostModel.id == instance.id)
            .values(
                title=instance.title,
                content=instance.content,
            )
        )
        result = await self.session.execute(query)
        if result.rowcount == 0:
            raise ObjectNotFound(f"Post with id {instance.id} not found")
        return instance

    async def delete(self, post_id: int) -> None:
        query = delete(PostModel).where(PostModel.id == post_id)
        result = await self.session.execute(query)
        if result.rowcount == 0:
            raise ObjectNotFound(f"Post with id {post_id} not found")

    @staticmethod
    def _to_dto(post: PostModel) -> PostDTO:
        print("Преобразуем объект в DTO:")
        return PostDTO(
            id=post.id,
            title=post.title,
            content=post.content,
            created_at=post.created_at,
            author=post.user.username,
        )

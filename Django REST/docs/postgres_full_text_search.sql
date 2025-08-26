-- Подключаем необходимые расширения
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS btree_gin;

-- Добавляем полнотекстовый поиск через индекс по двум полям
CREATE INDEX IF NOT EXISTS post_search_weighted_idx
ON posts
USING GIN (
   (
        setweight(to_tsvector('russian', coalesce(title, '')), 'A')
        ||
        setweight(to_tsvector('russian', coalesce(content, '')), 'B')
    )
);

-- Индекс для поиска по коротким словам
-- Для title
CREATE INDEX IF NOT EXISTS posts_title_trgm ON posts USING GIN (title gin_trgm_ops);
-- Для content
CREATE INDEX IF NOT EXISTS posts_content_trgm ON posts USING GIN (content gin_trgm_ops);

create table users (
	id bigint unsigned primary key auto_increment,  -- Уникальный идентификатор
	username varchar(64) unique not null,  -- длина 64 символа (обязательно для заполнения)
    password varchar(64) not null,
    phone varchar(20) null
);

-- Таблица для заметок пользователя
create table posts (
	id int unsigned primary key auto_increment,
    user_id bigint unsigned not null,  -- Для уникального ключа пользователя
    title varchar(200) default 'Заголовок не указан' not null,  -- Со значением по умолчанию
    created datetime not null,
    content text not null,

    -- Связываем таблицу пользователей (поле id) с полем user_id в текущей таблице.
    -- Создаем "внешний ключ".
    foreign key (user_id) references users (id)
);

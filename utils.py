import json

POST_PATH = "data/data.json"
COMMENTS_PATH = "data/comments.json"


def get_posts_all():  # возвращает посты
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_post_by_id():
    with open(COMMENTS_PATH, 'r', encoding='utf-8') as file:
        post_id = json.load(file)
    return post_id


def get_posts_by_user(user_name):  # Шаг 4
    # Возвращает посты определенного пользователя.
    # Функция должна вызывать ошибку ValueError если такого пользователя нет и пустой список,
    # если у пользователя нет постов.

    try:
        posts = []  # Создаем пустой список постов
        for post in get_posts_all():  # Проверяем есть ли такой User(Пользователь) в списке posts
            if user_name == post.poster_name:
                posts.append(post)  # Добавляем в список Пост Пользователя, который есть у нас в data.json.
            return posts  # Возвращаем список
        if len(posts) == 0:  # если постов 0, то возвращаем ValueError
            raise ValueError
    except ValueError:  # Выводим сообщение при ошибке
        return 'Нет такого пользователя'


def get_comments_by_post_id(post_id):  # post_id == pk(comments.json)?: Шаг 2
    # Возвращает комментарии определенного поста.
    # Функция должна вызывать ошибку ValueError если такого поста нет и пустой список
    # если у поста нет комментов.

    try:
        comments = []
        for comment in get_post_by_id():
            if post_id == comment.post_id:
                comments.append(comment)
            return comments
        if len(comments) == 0:
            raise ValueError
    except ValueError:
        return 'Нет такого комментария'


def search_for_posts(query):  # Возвращает список постов по ключевому слову: Шаг 5 и Шаг 3.
    if query in get_posts_all():
        pass


def get_post_by_pk(pk):  # Возвращает один пост по его идентификатору.
    pass

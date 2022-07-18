from flask import Flask, Blueprint, request, render_template
from utils import get_posts_all, get_post_by_id, get_comments_by_post_id, get_posts_by_user, search_for_posts

app = Flask(__name__)


@app.route('/')
def main():
    lists = get_posts_all()
    return render_template('index.html', posts=lists)


@app.route('/posts/<post_id>')
def render_post(post_id):
    post = get_post_by_id(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', posts=post, comments=comments)


@app.route('/users/<user_name>')  # Возвращает посты определенного пользователя.
def render_get_posts_by_user(user_name):
    post = get_posts_by_user(user_name)
    if post == 'Нет такого пользователя':
        return post
    return render_template('post.html', posts=post)


@app.route('/search/<query>')  # Возвращает список постов по ключевому слову: Шаг 5, Шаг 3
def render_search_for_post(query):
    query = request.args.get('s')
    search = search_for_posts(query)
    return render_template('search.html', query=query, posts=search)


app.run(debug=True)
# Создайте представление для всех постов, это должна быть главная страница.
#
# `GET` `/`
# в нем должно показываться столько постов, сколько есть. Найдите и используйте подходящий шаблон.
# Замените в каждом шаблоне пути к файлу стилей и картинкам.
# Замените их на /`static/img` и `/static/css` соответственно

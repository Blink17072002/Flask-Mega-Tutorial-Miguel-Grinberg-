from app import app, db

# print(app.config['SECRET_KEY'])
from app.models import User, Post
import sqlalchemy as sa
import sqlalchemy.orm as so

# app.app_context().push()
# u = User(username='john', email='john@example.com')
# u = User(username='susan', email='susan@example.com')

# print(u)
# db.session.add(u)
# db.session.commit()

# query = sa.select(User)
# users = db.session.scalars(query).all()
# for u in users:
#     print(u.id, u.username)

# u = db.session.get(User, 1)
# p = Post(body='my first post!', author=u)
# db.session.add(p)
# db.session.commit()

# get all posts written by a user
# u = db.session.get(User, 1)
# print(u)
# query = u.posts.select()
# posts = db.session.scalars(query).all()
# print(posts)

# print post author and body for all posts
# query = sa.select(Post)
# posts = db.session.scalars(query)
# for p in posts:
#     print(p.id, p.author.username, p.body)

# get all users in reverse alphabetical order
# query = sa.select(User).order_by(User.username.desc())
# names_desc = db.session.scalars(query).all()
# print(names_desc)

# get all users that have usernames starting with 's'
# query = sa.select(User).where(User.username.like('s%'))
# print(db.session.scalars(query).all())

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}
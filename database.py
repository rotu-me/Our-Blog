import os
from sqlalchemy import create_engine, text

my_secret = os.environ['DB_CONNECTION_STRING']
engine = create_engine(my_secret,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def get_posts():
  with engine.connect() as conn:
    result = conn.execute(text("select * from posts"))
    posts = []
    for post in result.all():
      posts.append(post)
    return posts
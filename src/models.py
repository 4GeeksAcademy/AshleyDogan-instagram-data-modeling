import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import create_engine, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))


class posts(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    captions: Mapped[str] = mapped_column(nullable=True)
    media: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    timestamp: Mapped[str] = mapped_column(nullable=False)
    tagged_friends: Mapped[int] = mapped_column(nullable=True)


class Comment(Base):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))

    def to_dict(self):
        return {}
    



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

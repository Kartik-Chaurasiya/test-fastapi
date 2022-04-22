from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key = True, nullable= False)
    user_id = Column(Integer,ForeignKey("users.user_id", ondelete="CASCADE"), nullable= False)
    title = Column(String, nullable= False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default = 'TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable =False, server_default = text('now()'))
    user = relationship("User")

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key = True, nullable= False)
    username = Column(String, nullable= False, unique=True)
    email = Column(String, nullable= False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable =False, server_default = text('now()'))

class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer,ForeignKey("users.user_id", ondelete="CASCADE"), primary_key= True)
    post_id = Column(Integer,ForeignKey("posts.post_id", ondelete="CASCADE"), primary_key= True)
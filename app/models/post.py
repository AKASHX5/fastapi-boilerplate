from app.db.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, text


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    published_at = Column(TIMESTAMP(timezone=True),
                          server_default=text('now()'))

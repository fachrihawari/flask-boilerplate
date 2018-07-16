from sqlalchemy import Column, Integer, String, Date, Text, Boolean

from bootstrap import db

class Page(db.Model):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False, unique=True)
    content = Column(Text)
    is_active = Column(Boolean, default=False)
    
    created_at = Column(Date)
    updated_at = Column(Date)
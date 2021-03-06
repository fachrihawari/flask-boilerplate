from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey

from .... import db

class Page(db.Model):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False, unique=True)
    content = Column(Text)
    is_active = Column(Boolean, default=False, server_default='False')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())

    def __repr__(self):
        return '<Page %r>' % self.title
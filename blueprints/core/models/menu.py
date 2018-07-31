from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, SmallInteger

from .... import db

class Menu(db.Model):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True)
    label = Column(String(35), nullable=False)
    target = Column(String, nullable=False) # path/link as menu target
    parent_id = Column(Integer) # make a menu as parent
    position = Column(SmallInteger) # position number of menu
    group = Column(String(30), nullable=False)
    is_active = Column(Boolean, default=False, server_default='False')

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())

    def __repr__(self):
        return '<Menu %r>' % self.label
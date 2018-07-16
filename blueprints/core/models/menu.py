from sqlalchemy import Column, Integer, String, Date, Boolean, SmallInteger

from bootstrap import db

class Menu(db.Model):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True)
    label = Column(String(35), nullable=False)
    target = Column(String, nullable=False) # path/link as menu target
    parent = Column(Integer) # make a menu as parent
    position = Column(SmallInteger) # position number of menu
    is_active = Column(Boolean, default=False)

    created_at = Column(Date)
    updated_at = Column(Date)

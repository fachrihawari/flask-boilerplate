from sqlalchemy import Column, Integer, String, Date, Boolean, Enum

from bootstrap import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(75))
    email = Column(String, unique=True, nullable=False)
    password = Column(String(60), nullable=False)

    role = Column(Enum('admin', 'member', name='user_role'), nullable=False, server_default='member')

    is_active = Column(Boolean, default=False)
    is_confirm = Column(Boolean, default=False)
    
    confirmation_token = Column(String(60))
    remember_token = Column(String(60))

    created_at = Column(Date)
    updated_at = Column(Date)
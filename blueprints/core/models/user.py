from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

from bootstrap import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String(60), nullable=False)

    is_active = Column(Boolean, default=False, server_default='False')
    is_confirm = Column(Boolean, default=False, server_default='False')
    
    confirmation_token = Column(String(60))
    remember_token = Column(String(60))
    
    role_id = Column(Integer, ForeignKey('roles.id'))

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())

class Permission(db.Model):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    parent_id = Column(Integer, ForeignKey('permissions.id', ondelete='cascade'))

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())

class PermissionRole(db.Model):
    __tablename__ = 'permission_role'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='cascade'), nullable=False)
    permission_id = Column(Integer, ForeignKey('permissions.id', ondelete='cascade'), nullable=False)

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
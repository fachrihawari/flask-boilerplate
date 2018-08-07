from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

from ..models.menu import Menu

class MenuForm(FlaskForm):
    label = StringField('Label', validators=[DataRequired(), Length(max=35)])
    target = StringField('Target', validators=[DataRequired()])
    parent_id = SelectField('Parent')
    position = IntegerField('Position')
    group = StringField('Group', validators=[DataRequired(), Length(max=30)])
    icon = StringField('Icon', validators=[Length(max=30)])
    is_active = BooleanField('Is Active')
    submit = SubmitField()
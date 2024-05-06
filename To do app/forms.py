from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField,BooleanField
from wtforms.validators import DataRequired

# top section of task form
class TaskForm(FlaskForm):
    description = StringField("Task description", validators=[DataRequired()])
    task_date = DateField("Date",format='%Y-%m-%d', validators=[DataRequired()])
    reminder = BooleanField("Reminder")
    submit = SubmitField("Submit task")


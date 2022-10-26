from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, DateField, validators, ValidationError
from .models import Position, Employee

class PositionForm(FlaskForm):
    name=StringField(label='Имя')#,validators=[validators.DataRequired]
    department=StringField(label='Департамент')#,validators=[validators.DataRequired]
    wage=IntegerField(label='Зарплата')
    submit = SubmitField(label='Сохранить позицию')

def validate_wage(self,wage):
    if wage.data < 0:
        raise ValidationError('Зарплата не может быть отрицательной')

class EmployeeForm(FlaskForm):
    name = StringField(label='Имя сотрудника')
    birth_date = IntegerField(label='Дата рождения сотрудника')
    position_id = SelectField(label='Позиция')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for position in Position.query.all():
            result.append((position.id, position.name))
        self.position_id.choices = result

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for employee in Employee.query.all():
            result.append((employee.id, employee.name))
        self.employee_id.choices = result
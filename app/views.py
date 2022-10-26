import datetime

from flask import render_template, request, redirect, url_for, flash
from . import app, db
from .models import Position, Employee
from .forms import PositionForm, EmployeeForm

def index():
    title='Список сотрудников'
    employees = Employee.query.all()
    return render_template('index.html', employees=employees, title=title)
def position_create():
    title='Сохранение позиции'
    form = PositionForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            position=Position()
            form.populate_obj(position)
            db.session.add(position)
            db.session.commit()
            flash(f'Позиция {position.id} успешно сохранена','success')
        else:
            for field, errors in form.errors.positions():
                for error in errors:
                    flash(f'Ошибка в поле "{field}" текст ошибки "{error}"', 'danger')
    return render_template('position_form.html', form=form, title=title)

def position_delete():
    if request.method == 'GET':
        return render_template('position_delete.html')
    if request.method == 'POST':
        db.session.delete(position)
        db.session.commit()
        return redirect(url_for('position'))

def position_update(position_id):
    position=Position.query.filter_by(id=position_id).first()
    form=PositionForm(request.form,obj=position)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(position)
            db.session.commit()
            flash(f'Позиция под номером {position.id} успешно обновлена', 'success')
            return redirect(url_for('index'))
        else:
            for field, errors in form.errors.positions():
                for error in errors:
                    flash(f'Ошибка в поле "{field}" текст ошибки "{error}"', 'danger')
    return render_template('position_form.html', form=form, position=position)

def employee_create():
    title = 'Сохранение сотрудника'
    form = EmployeeForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            employee = Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash(f'Позиция {employee.id} успешно сохранена', 'success')
        else:
            for field, errors in form.errors.employees():
                for error in errors:
                    flash(f'Ошибка в поле "{field}" текст ошибки "{error}"', 'danger')
    return render_template('employee_form.html', form=form, title=title)

def employee_detail(employee_id):
    employee=Employee.query.filter_by(id=employee_id).first()
    return render_template('employee_detail.html', employee=employee)


def employee_delete():
    if request.method == 'GET':
        return render_template('employee_delete.html')
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        flash(f'Данные о работниках {employee.id} успешно удален', 'success')
        return redirect(url_for('employee'))


def employee_update(employee_id):
    employee=Employee.query.filter_by(id=employee_id).first()
    form = EmployeeForm(request.form, obj=employee)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(employee)
            db.session.commit()
            flash(f'Позиция под номером {employee.id} успешно обновлена', 'success')
            return redirect(url_for('employee_form.html', employee_id=employee.id))
        else:
            for field, errors in form.errors.employees():
                for error in errors:
                    flash(f'Ошибка в поле "{field}" текст ошибки "{error}"', 'danger')
        return render_template('employee_form.html', form=form, employee=employee)






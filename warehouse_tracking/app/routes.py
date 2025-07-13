from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Employee, Task
from app import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    # Get metrics for dashboard
    total_tasks = Task.query.count()
    completed_tasks = Task.query.filter_by(status='Completed').count()
    pending_tasks = Task.query.filter_by(status='Pending').count()
    in_progress_tasks = Task.query.filter_by(status='In Progress').count()
    
    employees = Employee.query.all()
    
    # Task completion rate
    completion_rate = 0
    if total_tasks > 0:
        completion_rate = (completed_tasks / total_tasks) * 100
    
    # Get tasks by type for chart
    task_types = db.session.query(Task.task_type, db.func.count(Task.id)).group_by(Task.task_type).all()
    
    # Get productivity data (tasks completed per employee)
    productivity = db.session.query(
        Employee.name, 
        db.func.count(Task.id)
    ).join(Task).filter(Task.status == 'Completed').group_by(Employee.name).all()
    
    return render_template('dashboard.html', 
                         total_tasks=total_tasks,
                         completed_tasks=completed_tasks,
                         pending_tasks=pending_tasks,
                         in_progress_tasks=in_progress_tasks,
                         completion_rate=round(completion_rate, 2),
                         employees=employees,
                         task_types=task_types,
                         productivity=productivity)

@main.route('/tasks')
def tasks():
    all_tasks = Task.query.order_by(Task.due_date).all()
    return render_template('tasks.html', tasks=all_tasks)

@main.route('/employees')
def employees():
    all_employees = Employee.query.all()
    return render_template('employees.html', employees=all_employees)

@main.route('/api/task_status_data')
def task_status_data():
    status_counts = {
        'Completed': Task.query.filter_by(status='Completed').count(),
        'Pending': Task.query.filter_by(status='Pending').count(),
        'In Progress': Task.query.filter_by(status='In Progress').count(),
        'Cancelled': Task.query.filter_by(status='Cancelled').count()
    }
    return jsonify(status_counts)

@main.route('/api/task_type_data')
def task_type_data():
    task_types = db.session.query(Task.task_type, db.func.count(Task.id)).group_by(Task.task_type).all()
    result = {t[0]: t[1] for t in task_types}
    return jsonify(result)

@main.route('/api/employee_performance')
def employee_performance():
    performance = db.session.query(
        Employee.name,
        db.func.count(Task.id),
        db.func.sum(Task.estimated_time),
        db.func.sum(Task.actual_time)
    ).join(Task).filter(Task.status == 'Completed').group_by(Employee.name).all()
    
    result = []
    for p in performance:
        efficiency = 0
        if p[3] and p[2]:  # if actual_time and estimated_time exist
            efficiency = (p[2] / p[3]) * 100
        result.append({
            'name': p[0],
            'tasks_completed': p[1],
            'efficiency': round(efficiency, 2)
        })
    
    return jsonify(result)
from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

class Employee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'manager', 'supervisor', 'worker'
    department = db.Column(db.String(50))
    tasks = db.relationship('Task', backref='assigned_to', lazy=True)
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default='Pending')  # Pending, In Progress, Completed, Cancelled
    priority = db.Column(db.String(20))  # Low, Medium, High, Critical
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    location = db.Column(db.String(100))  # Warehouse location
    task_type = db.Column(db.String(50))  # Picking, Packing, Inventory, Receiving, etc.
    estimated_time = db.Column(db.Integer)  # in minutes
    actual_time = db.Column(db.Integer)  # in minutes
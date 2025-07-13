from app import create_app, db
from app.models import Employee, Task
from datetime import datetime, timedelta

app = create_app()

def add_sample_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Add employees
        employees = [
            Employee(name='John Doe', email='john@example.com', password='password', role='worker', department='Picking'),
            Employee(name='Jane Smith', email='jane@example.com', password='password', role='supervisor', department='Packing'),
            Employee(name='Mike Johnson', email='mike@example.com', password='password', role='worker', department='Inventory'),
            Employee(name='Sarah Williams', email='sarah@example.com', password='password', role='manager', department='Management')
        ]
        
        for emp in employees:
            db.session.add(emp)
        db.session.commit()

        # Add tasks
        tasks = [
            Task(
                title='Pick order #1001',
                description='Pick items for customer order #1001',
                status='Completed',
                priority='High',
                due_date=datetime.utcnow() - timedelta(days=1),
                completed_at=datetime.utcnow() - timedelta(hours=12),
                employee_id=1,
                location='Aisle 3, Shelf B',
                task_type='Picking',
                estimated_time=30,
                actual_time=25
            ),
            Task(
                title='Pack order #1002',
                description='Pack items for customer order #1002',
                status='In Progress',
                priority='Medium',
                due_date=datetime.utcnow() + timedelta(days=1),
                employee_id=2,
                location='Packing Station 1',
                task_type='Packing',
                estimated_time=45,
                actual_time=None
            ),
            Task(
                title='Inventory check - Section A',
                description='Perform inventory check for Section A',
                status='Pending',
                priority='Low',
                due_date=datetime.utcnow() + timedelta(days=3),
                employee_id=3,
                location='Section A',
                task_type='Inventory',
                estimated_time=120,
                actual_time=None
            )
        ]
        
        for task in tasks:
            db.session.add(task)
        db.session.commit()

if __name__ == '__main__':
    add_sample_data()
    print("Sample data added successfully!")
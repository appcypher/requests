from models import Staff
from models.db import db


def seed_staff():
    staffs = [
        Staff(id=1, username='Steve Akinyemi', avatar_url=''),
        Staff(id=2, username='James Cameron', avatar_url=''),
        Staff(id=3, username='John Does', avatar_url=''),
    ]
    db.session.add_all(staffs)
    db.session.commit()

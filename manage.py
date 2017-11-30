from flask_script import Manager
from my_resume import app, db, Professor, Course

manager = Manager(app)


# reset the database and populate with two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    everard = Professor(name='Andrea Everard', department='MIS')
    hartono = Professor(name='Edward Hartono', department='MIS')
    course1 = Course(course_number='MISY160', title='Business Computing: Tools and Concepts', description='Introduction to computers: components and operations.', professor=hartono)
    course2 = Course(course_number='MISY225', title='Introduction to Programming Business Applications', description='Use of higher level contemporary computing languages to structure Prototyping applications of systems.', professor=hartono)
    course3 = Course(course_number='MISY427', title='Management of Information Systems', description='Explores practical applications of information technology in all aspects of management.', professor=everard)
    course4 = Course(course_number='MISY431', title='MIS Project Management', description='Students learn project management techniques, and working in teams, apply this knowledge by developing technology-based business solutions for various enterprises.', professor=everard)
    db.session.add(hartono)
    db.session.add(everard)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()

from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        """Enroll the student in a course"""
        from __main__ import Course, Enrollment  # local import avoids circular issues if needed
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        """Return a copy of enrollments"""
        return self._enrollments.copy()

    # Aggregate example: count of enrollments
    def enrollment_count(self):
        return len(self._enrollments)


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        """Add an enrollment to this course"""
        from __main__ import Enrollment
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        """Return a copy of enrollments"""
        return self._enrollments.copy()

    # Aggregate example: number of students enrolled
    def student_count(self):
        return len(self._enrollments)


class Enrollment:
    all = []

    def __init__(self, student, course):
        from __main__ import Student, Course
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    # Class method: aggregate enrollments per day
    @classmethod
    def aggregate_enrollments_per_day(cls):
        """Return a dictionary of enrollment counts per day"""
        counts = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            counts[date] = counts.get(date, 0) + 1
        return counts

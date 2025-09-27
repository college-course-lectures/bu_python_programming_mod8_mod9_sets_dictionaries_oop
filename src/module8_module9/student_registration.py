import pickle
'''
Professor Lewis
Python Sets, Dictionaries and Object-Oriented Programming
September26, 2025
'''

class Student:

    def __init__(self, name, sid):
        self._name  = name.strip()
        self._sid = str(sid).strip()

    # getters/setters
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = str(value).strip()

    def get_sid(self):
        return self._sid
    def set_sid(self, value):
        self._sid = str(value).strip()

    # string representation
    def __str__(self):
        return f"Student(name='{self._name}', id='{self._sid}')"


class Course:
    def __init__(self, code, title=""):
        self._code = code.strip().upper()
        self._title = title.strip()

    #basic getters/setters
    def get_code(self):
        return self._code
    def set_code(self, value):
        self._code = str(value).strip().upper()

    def get_title(self):
        return self._title
    def set_title(self, value):
        self._title = str(value).strip()

    #string representation
    def __str__(self):
        return f"{self._code}" + (f" - {self._title}" if self._title else "")


class Registrar:
    def __init__(self):
        self.students = {}
        self.courses = set()
        self.enrollments = {}

    def add_student(self, s):
        sid = s.get_sid()
        name = s.get_name()
        if not sid or sid in self.students:
            raise ValueError("Bad/dup student ID")
        self.students[sid] = name
        self.enrollments[sid] = set()

    def add_course(self, c):
        code = c.get_code()
        if not code or code in self.courses:
            raise ValueError("Bad/dup course code")
        self.courses.add(code)

    def enroll(self, sid, code):
        sid = str(sid).strip()
        code = str(code).strip().upper()
        if sid not in self.students:
            raise KeyError("No such student")
        if code not in self.courses:
            raise KeyError("No such course")
        self.enrollments[sid].add(code)

    def is_enrolled(self, student_id, course_code):
        student_id = str(student_id).strip()
        course_code = str(course_code).strip().upper()

        if student_id not in self.enrollments:
            return False

        return course_code in self.enrollments[student_id]

    def save_enrollments(self, filepath):

        with open(filepath, "wb") as f:
            pickle.dump(self.enrollments, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load_enrollments(self, filepath):
        try:
            with open(filepath, "rb") as f:
                self.enrollments = pickle.load(f)
            print("Enrollments loaded successfully.")
        except FileNotFoundError:
            print("No saved enrollments file found.")
        except Exception as e:
            print("Error loading enrollments:", e)

    def print_enrollment_preview(reg):
        preview = {sid: list(courses) for sid, courses in reg.enrollments.items()}
        print("\n-- Enrollment Preview --")
        print(preview)
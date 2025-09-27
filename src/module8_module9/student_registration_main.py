from student_registration import Registrar, Course, Student
'''
Professor Lewis
Python Sets, Dictionaries and Object-Oriented Programming
September 26, 2025
'''

def main():
    reg = Registrar()
    print("Registrar (students=dict, courses=set and enrollments=dict stuID: list of courses enrolled)")

    # Courses
    num_courses = int(input("How many courses? ") or 0)
    for i in range(1, num_courses+1):
        code = input(f"Course {i} code (ex. CS1, CS2): ").strip().upper()
        title = input("  Title: ").strip()
        try:
            new_course = Course(code, title)
            reg.add_course(new_course)
        except Exception as e:
            print("  Skipped:", e)

    # Students
    number_students = int(input("\nHow many students? ") or 0)
    for i in range(1, number_students+1):
        name = input(f"Student {i} name: ").strip()
        sid  = input("  ID: ").strip()
        try:
            new_student = Student(name, sid)
            reg.add_student(new_student)
        except Exception as e:
            print("  Skipped:", e)

    # Enrollments
    print("\nEnter enrollments one per line as S:COURSE (ex., S1:CS1).")
    print("Press Enter on a blank line to finish.")

    while True:
        pair = input("Enrollment pair: ").strip()
        if not pair:
            break

        if ":" not in pair:
            print("  Skipped: format must be S:COURSE (ex.,S1 :CS1)")
            continue

        sid, code = pair.split(":", 1)
        sid = sid.strip()
        code = code.strip()

        try:
            reg.enroll(sid, code)
        except Exception as e:
            print("  Skipped:", e)


    # Output (compact)
    print("\nCourses:", ", ".join(sorted(reg.courses)) or "(none)")
    print("Students:", ", ".join(f"{sid}:{name}" for sid, name in reg.students.items()) or "(none)")
    print("Enrollments:")
    for sid in reg.students:
        print(f"  {sid}: {sorted(reg.enrollments.get(sid, set()))}")



    #Enrollment check
    print("\nCheck if a student is enrolled in a course.")
    student_id = input("Enter student ID to search: ").strip()
    course_code = input("Enter course code to search: ").strip()

    if reg.is_enrolled(student_id, course_code):
        print(f"Student {student_id} is enrolled in {course_code}")
    else:
        print("Not enrolled")


    #Save enrollments - Serialize - pickle file
    reg.save_enrollments("enrollments.pkl")
    print("Saved enrollments to enrollments.pkl")

    # Load enrollments
    reg.load_enrollments("enrollments.pkl")
    reg.print_enrollment_preview()


if __name__ == "__main__":
    main()
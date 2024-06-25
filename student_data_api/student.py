class Student:

    def __init__(self, fname, lname, major, ch, gpa, id):
        self._fname = fname
        self._lname = lname
        self._major = major
        self._ch = int(ch)
        self._gpa = gpa
        self._id = id
        self.get_class_level()

    def __str__(self):
        return f"{self._class} {self._fname} {self._lname}:\n\nMajor: {self._major}, Credit Hours: {self._ch}\nGPA: {self._gpa}, ID: {self._id}\n"

    def get_class_level(self):

        if self._ch > 90:
            self._class = "Senior"
        elif self._ch >= 61:
            self._class = "Junior"
        elif self._ch >= 31:
            self._class = "Sophomore"
        elif self._ch >= 0:
            self._class = "Freshman"

    def update_credit_hours(self, added_hours):
        self._ch += added_hours
        self.get_class_level()
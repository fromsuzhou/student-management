# -*- coding: utf-8 -*-
import json

from ..models.student import Student
class JsonStorage:
    def __init__(self, filepath):
        self.path=filepath

    def save(self, students):
        student_list = []
        for student in students:
            student_list.append(student.to_dict())
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(student_list, file, ensure_ascii=False, indent=2)

    def load(self):
        with open(self.path, "r", encoding="utf-8") as file:
            dict_list = json.load(file)
        student_list = []
        for student in dict_list:
            student_list.append(Student.from_dict(student))
        return student_list
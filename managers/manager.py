# -*- coding: utf-8 -*-
import json
from ..models.student import Student
class StudentManager:
    def __init__(self):
        self.students=[]

    def add_student(self):
        print("请输入学生姓名和成绩：")
        name,score=input().split()
        s=Student(name, int(score))
        if s not in self.students:
            self.students.append(s)
            print("添加成功!")

    def show_student(self):
        for s in self.students:
            print(s)

    def search_student(self,name):
        for s in self.students:
            if s.name==name:
                return s
        return None

    def modify_student(self,name,score):
        s=self.search_student(name)
        if s is None:
            return False
        s.score=score
        return True

    def delete_student(self,name):
        student=self.search_student(name)
        if student is None:
            return False
        self.students.remove(student)
        return True

    def set_students(self, students):
        self.students = students
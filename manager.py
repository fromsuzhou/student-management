# -*- coding: utf-8 -*-
import json

from student import Student
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

    def save(self):
        student_list = []
        for student in self.students:
            student_list.append(student.to_dict())
        with open("student_management.txt", "w", encoding="utf-8") as file:
            json.dump(student_list, file, ensure_ascii=False, indent=2)

    def load(self):
        try:
            with open("student_management.txt", "r", encoding="utf-8") as file:
                data = json.load(file)
            self.students=[]
            for student_data in data:
                self.students.append(Student.from_dict(student_data))
        except FileNotFoundError:
            self.students = []
            print("提示：未找到数据文件，使用空白学生列表")
        except json.JSONDecodeError:
            self.students = []
            print("提示：数据文件JSON格式损坏，使用空白学生列表")
        except KeyError:
            self.students = []
            print("提示：文件中学生数据字段缺失，使用空白学生列表")
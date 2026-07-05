# -*- coding: utf-8 -*-
class Student:
    def __init__(self, name, score):
        self.name=name
        self.score=score

    def to_dict(self):
        return {
            "name": self.name,
            "score": self.score
        }

    def __str__(self):
        return f"姓名：{self.name}\n分数：{self.score}"

    @classmethod
    def from_dict(cls,data):
        return cls(data["name"],data["score"])

    def __repr__(self):
        return f"Student(name='{self.name}', score={self.score})"
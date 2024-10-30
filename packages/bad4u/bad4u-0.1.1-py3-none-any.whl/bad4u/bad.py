#!/usr/bin/env python3

class Skills:

    def __init__(self, skills, level, hours):
        self.skills = skills
        self.level = level
        self.hours = hours

    def __repr__(self):
        return f"{self.skills} Level [{self.level}] Horas [{self.hours}]"

skill = [
    Skills("Scripting", 40, 23),
    Skills("Pentester", 10, 5),
    Skills("Hacker Justiciero", 4, 2)
]

def list_skills():

    for element in skill:
        print(element)

def search_skill(name):

    for element in skill:

        if name == element.skills:
            return element
    else:
        return None



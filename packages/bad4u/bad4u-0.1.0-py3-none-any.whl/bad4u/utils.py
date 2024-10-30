from .bad import skill

def total_duration():
    total = sum(element.hours for element in skill)
    print(f"{total} horas")

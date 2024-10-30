# Upload Test for Pipy

Esta es una biblioteca de prueba

## Stats de skills

- Scripting [level 40] [23 horas]
- Pentester [level 10] [5 horas]
- Hacker justiciero [level 4] [2 horas]

## Instalacion

Instala el paquete usando `pip3`:

```python3
pip3 install bad4u
```

## Uso basico

### Listar todas las skills

```python
from bad4u import list_skills

for element in list_skills():
    print(element)
```

### Listar skill por nombre

```python
from bad4u import search_skill

skill = search_skill("Scripting")
print(skill)
```

### Calcular total de horas

```python3
from bad4u.utils import total_duration

print(f"Duracion total: {total_duration()} horas")
```

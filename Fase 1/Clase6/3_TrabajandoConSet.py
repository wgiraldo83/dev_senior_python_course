# Los set sólo permiten ingresar o eliminar datos
lenguajes = {"Java", "Python", "JavaScript"}
print(lenguajes)
print(len(lenguajes))
print("Java" in lenguajes)
lenguajes.add("Go")
print(lenguajes)
for lenguaje in lenguajes:
    print(lenguaje)
lenguajes.remove("Java")
print(lenguajes)
lenguajes.discard("Python")
print(lenguajes)

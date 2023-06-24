from django.shortcuts import render

books = [
    {
        "id": "1",
        "editorial": "Editorial 1",
        "pais": "Chile",
        "fecha": "2021-10-10",
        "autor": "Juan",
        "titulo": "El libro de Juan",
        "descripcion": "Este es el libro de Juan",
        "materia": "Matematicas",
        "año": "2021",        
    },
    {
        "id": "2",
        "editorial": "Editorial 2",
        "pais": "Cuba",
        "fecha": "2021-11-10",
        "autor": "Ari",
        "titulo": "El libro de Ari",
        "descripcion": "Este es el libro de Ari",
        "materia": "Lenguaje",
        "año": "2022",        
    },
    {
        "id": "3",
        "editorial": "Editorial 2",
        "pais": "Cuba",
        "fecha": "2021-11-10",
        "autor": "Ari",
        "titulo": "El 2do libro de Ari",
        "descripcion": "Este es el libro de Ari 2",
        "materia": "Programacion",
        "año": "2022",        
    },
    {
        "id": "4",
        "editorial": "Editorial 1",
        "pais": "Chile",
        "fecha": "2021-10-10",
        "autor": "Alberto",
        "titulo": "El libro de Alberto",
        "descripcion": "Este es el libro de Alberto",
        "materia": "Matematicas",
        "año": "2021",        
    },
]

prestados = [{
   "id_libro": "1",
   "fecha_devolucion": "2021-10-10",
   "fecha_prestamo": "2021-10-10",
}]

def index(request):
   return render(request, "home.html")

def all(request):
   return render(request, "books.html",{"books":books})

def book(request):
   id = request.GET.get("id")   
   partial = filter(lambda e: e["id"] == id,books)
   partial = list(partial)
   return render(request, "book.html",{"books":partial})

def materia(request):
   materia = request.GET.get("materia")
   partial = filter(lambda e: e["materia"] == materia,books) #SQL a la BD
   return render(request, "books.html",{"books":partial})

def autor(request):
   autor = request.GET.get("autor")
   partial = filter(lambda e: e["autor"] == autor,books)
   return render(request, "books.html",{"books":partial})

def prestado(request):
   prestaSet = list(map(lambda e: e["id_libro"] ,prestados))
   partial = filter(lambda e: e["id"] in prestaSet ,books) #SQL a la BD
   partial = list(partial)
   return render(request, "books.html",{"books":partial})
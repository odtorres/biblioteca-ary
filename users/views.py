from django.shortcuts import render

# Create your views here.
users = [
    {
        "id": "1",
        "nombre": "Juan",
        "apellido": "Perez",
        "ci": "1234567",
        "telefono": "1234567",
        "direccion": "Calle 1",
        "email": "",
        "año": "2021",
    },
]

def index(request):
   return render(request, "sancionados.html",{"users":users})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from  tareas.views import tareas_lista

# Create your views here.
def resumen(request):
    global tareas_lista
    total = len(tareas_lista)
    contador_alta = 0
    contador_media = 0
    contador_baja = 0
    for tarea in tareas_lista:
        if tarea['prioridad'] == 'alta':
            contador_alta +=1
        elif tarea['prioridad'] == 'media':
            contador_media +=1
        else:
            contador_baja +=1
    
    html_content = f'''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Total de Tareas</title>
        </head>
        <body>
            <h1>Total de Tareas</h1>
            <p>Total: {total}</p>
            <p>Tareas prioridad alta: {contador_alta}</p>
            <p>Tareas prioridad media: {contador_media}</p>
            <p>Tareas prioridad baja: {contador_baja}</p>
            <a href='/'>Volver</a>
        </body>
    </html>
    '''

    return HttpResponse(html_content)
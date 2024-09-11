from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
# Lista global para almacenar las tareas (sólo para fines demostrativos)
tareas_lista = []

def agregar_tarea(request):
    global tareas_lista
    if 'nombre' in request.GET:
        nombre = request.GET.get('nombre')
        prioridad = request.GET.get('prioridad')
        tareas_lista.append({'nombre': nombre, 'prioridad':prioridad})
        return redirect('')

    tareas_html = '<ul>'
    for tarea in tareas_lista:
        
        tareas_html += f'<li>{tarea["nombre"]} - Prioridad:  {tarea["prioridad"]}</li>'
    tareas_html += '</ul>'

    form_html = '''
        <h2>Crear Tarea</h2>
        <form method="get" action="">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required><br>
            <label for="prioridad">Prioridad:</label>

            <label for="alta">Alta</label>
            <input type="radio" value="alta" id="prioridad" value="alta" name="prioridad">
            
            <label for="media">Media</label>
            <input type="radio" value="media" id="prioridad" value="media" name="prioridad" checked>

            <label for="baja">Baja</label>
            <input type="radio" value="baja" id="prioridad" value="baja" name="prioridad">
            <button type="submit">Guardar</button>
        </form>
    '''
    
    html_content = f'''
        <!DOCTYPE html>
        <html>
            <head>
                <title>Lista y Crea Tareas</title>
            </head>
            <body>
                <h1>Lista de Tareas</h1>
                {tareas_html}
                {form_html}
                <a href='resumen'>Ver Resumen</a>
            </body>
        </html>
    '''
    return HttpResponse(html_content)
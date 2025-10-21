from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def analizar_codigo(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '').strip()  # <-- 'codigo' debe coincidir con name del textarea
        if not codigo:
            return JsonResponse({'error': 'No se recibió ningún código.'})

        try:
            lines = codigo.splitlines()
            resultados = []
            variables = {}

            for linea in lines:
                if "=" in linea and "print" not in linea:
                    var, val = linea.split("=")
                    var = var.strip()
                    val = eval(val, {}, variables)
                    variables[var] = val
                elif "print" in linea:
                    expr = linea.replace("print", "").strip("() ")
                    resultados.append(str(eval(expr, {}, variables)))

            if not resultados:
                resultados.append("<sin salida>")

            return JsonResponse({'resultados': resultados})

        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Solo se aceptan peticiones POST'})


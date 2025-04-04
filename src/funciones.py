
# Calcula puntaje bajo la lógica: 3 puntos por kill, 1 por asistencia y 1 restado por muerte
def calcular_puntaje (kills, assist, dead):
        score= kills * 3 + assist - (1 if dead else 0)
        return score

# Proceso una ronda para devolverla con los MVP's y ordenada de forma descendente
def procesar_ronda(ronda):
    # Genero una lista vacía que voy a cargar con tuplas con los datos de cada jugador
    datos = []
    
    # Recorro los diccionarios de cada ronda cargando el código y obteniendo el valor
    for jugador, stats in ronda.items():
        kills = stats['kills']
        assists = stats['assists']
        deaths = stats['deaths']
        puntos = calcular_puntaje(kills, assists, deaths) # Llamo a mi función que calcula los puntos
        datos.append((jugador, kills, assists, deaths, puntos)) # Cargo a la lista tuplas con los datos de cada jugador
    
    max_puntos = max(p[4] for p in datos) # Compara los puntos de cada jugador y devuelve el máximo
    mvps_ronda = [jugador for jugador, _, _, _, puntos in datos if puntos == max_puntos] # Guardo al que salió MVP en cada ronda para usarlo en la impresión final
    datos_ordenados = sorted(datos, key=lambda x: x[4], reverse=True) # Ordeno los datos de forma descendente
    return datos_ordenados, mvps_ronda


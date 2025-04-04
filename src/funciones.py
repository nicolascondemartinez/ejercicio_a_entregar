
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

# Imprimo una ronda respetando el formato
def imprimir_ronda(numero, datos_ronda):
    print(f"\n Ranking ronda {numero}:")
    print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<10} {'Muerte':<8} {'Puntos':<6}")  # Trabajo el formato de impresión del programa
    print("-" * 75)
    for jugador, kills, assists, deaths, puntos in datos_ronda:
        muerte_str = "Sí" if deaths else "No" # Transforma en string el booleano muerte
        print(f"{jugador:<10} {kills:<6} {assists:<10} {muerte_str:<8} {puntos:<6}")

# Voy a recibir un diccionario de totales al que voy a cargar con los datos de cada jugador por ronda para facilitar su impresión
def actualizar_totales(totales, ronda):
    for jugador, stats in ronda.items():
        if jugador not in totales:
            totales[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0}
        totales[jugador]['kills'] += stats['kills']
        totales[jugador]['assists'] += stats['assists']
        if stats['deaths']:
            totales[jugador]['deaths'] += 1


# Defino la tabla final pedida agregando MVP's y Puntos totales
def imprimir_totales(totales, mvps):
    print("\n Ranking final:")
    print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<10} {'Muertes':<8} {'MVPs':<5} {'Puntos':<6}")
    print("-" * 84)
    jugadores = sorted(totales.items(), key=lambda j: calcular_puntaje(
        j[1]['kills'], j[1]['assists'], j[1]['deaths']), reverse=True) 
    
    for jugador, stats in jugadores:
        kills = stats['kills']
        assists = stats['assists']
        deaths = stats['deaths']
        mvp_count = mvps.get(jugador, 0)
        puntos = calcular_puntaje(kills, assists, deaths)
        print(f"{jugador:<10} {kills:<6} {assists:<10} {deaths:<8} {mvp_count:<5} {puntos:<6}")

# Utilizo una función que llame a todas las otras funciones pasandole los datos y de manera ordenada
def imprimir_total(rounds):
    totales = {} # Creo el diccionario de los datos totales
    mvps = {jugador: 0 for jugador in rounds[0]} # Inicializo una lista de diccionarios con valor 0 para cargar los MVP's

    for i, ronda in enumerate(rounds):
        datos_ronda, mvps_ronda = procesar_ronda(ronda)
        imprimir_ronda(i + 1, datos_ronda)
        actualizar_totales(totales, ronda)
        for jugador in mvps_ronda:
            mvps[jugador] += 1

    imprimir_totales(totales, mvps)


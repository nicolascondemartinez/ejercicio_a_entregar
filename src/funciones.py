
def puntaje (kills, assist, dead):
        score= kills * 3 + assist - (1 if dead else 0)
        return score

def tabla_de_puntajes(rounds):
    for i, ronda in enumerate(rounds):
        print(f"\n Ronda {i+1}")
        print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<10} {'Muertes':<8} {'Puntos':<6}")
        print("-" * 45)

        # Crear lista de tuplas con estadísticas por ronda
        estadisticas = [
            (jugador, stats['kills'], stats['assists'], "Sí" if stats['deaths'] else "No", puntaje(stats['kills'], stats['assists'], stats['deaths']))
            for jugador, stats in ronda.items()
        ]
        
        
        # Ordenar por puntos en orden descendente
        estadisticas.sort(key=lambda x: x[4], reverse=True)

        # Imprimir estadísticas de la ronda
        for jugador, kills, assists, deaths, puntos in estadisticas:
            print(f"{jugador:<10} {kills:<6} {assists:<10} {deaths:<8} {puntos:<6}")
        

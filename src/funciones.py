
def puntaje (kills, assist, dead):
        score= kills * 3 + assist - (1 if dead else 0)
        return score


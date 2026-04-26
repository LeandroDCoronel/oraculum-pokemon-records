def classify_iv(iv: int):
    if iv >= 90:
        return "Excelente"
    elif iv >= 70:
        return "Bueno"
    elif iv >= 50:
        return "Promedio"
    else:
        return "Malo"


def recommendation(iv: int):
    if iv >= 90:
        return "Invertir recursos (subir nivel / competitivo)"
    elif iv >= 70:
        return "Usable, pero no óptimo"
    elif iv >= 50:
        return "Solo para colección"
    else:
        return "Transferir"
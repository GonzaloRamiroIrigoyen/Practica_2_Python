def max_goleador(lista_nombres,lista_goles):
    indice=lista_goles.index(max(lista_goles))
    return (lista_nombres[indice],lista_goles[indice])


def mas_influyente(estruc):
    influencia=-1
    nom="----"
    for i in range(len(estruc["Nombres"])):
        contador=estruc["Goles"][i]*1.5+estruc["Evitados"][i]*1.25+estruc["Asistencias"][i]
        if contador>influencia :
            nom=estruc["Nombres"][i] 
            influencia=contador
    return nom

prom_goles=lambda cant_goles: cant_goles/25
    

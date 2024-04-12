def crear_estructura(names, goals, goals_avoided, assists):
    caracteres_especiales=[" ","'","\n"]
    for car in caracteres_especiales:
        names=names.replace(car,"")
    names=names.split(",")
    return {"Nombres":names, "Goles":goals,"Evitados":goals_avoided, "Asistencias":assists}
    
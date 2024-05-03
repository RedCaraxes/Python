"""
/*
 * ¡Han anunciado un nuevo "The Legend of Zelda"!
 * Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
 * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
 * "The Legend of Zelda" de la historia?
 * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
 * que tú selecciones.
 * - Debes buscar cada uno de los títulos y su día de lanzamiento 
 *   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
 */
"""
import datetime

def diffDate_lanzamiento(date1, date2):
    date_format = '%d/%m/%Y-%H:%M:%S'
    date1 = datetime.datetime.strptime(date1, date_format)
    date2 = datetime.datetime.strptime(date2, date_format)
    
    diferencia_total = abs(date1 - date2)
    diferencia_en_horas = diferencia_total.total_seconds() / 3600

    dias = int(diferencia_en_horas // 24)
    horas_restantes = int(diferencia_en_horas % 24)
    minutos_restantes = int((diferencia_total.seconds % 3600) / 60)
    
    return print(f"La diferencia es de {dias} días, {horas_restantes} horas y {minutos_restantes} minutos.")

# Ejemplo de uso:
diffDate_lanzamiento('01/08/2023-12:50:00', '08/08/2023-8:30:00')

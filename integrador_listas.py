'''
Estás organizando la música de una fiesta y usas una lista de Python para llevar el control
de las canciones. Antes de empezar a modificar la lista, quieres guardar una copia de
seguridad por si algo sale mal. Durante la noche va pasando lo siguiente: un invitado pide
una canción, así que la agregas al final de la lista. Luego un amigo te comparte su propia
lista de canciones favoritas y decides sumarlas todas de una vez a la playlist. Alguien más
llega tarde pero pide que su canción suene primero, así que la insertas al inicio de la lista.
Más tarde, uno de los invitados que pidió una canción se va de la fiesta y ya no quiere que
su canción suene, así que la eliminas de la lista. La canción que está sonando en ese
momento termina y la retiras de la lista (y quieres guardar cuál era, por si alguien pregunta).
Quieres saber en qué posición quedó una canción específica dentro de la playlist actual, y
también cuántas veces se repitió el nombre de una canción que varios invitados pidieron sin
darse cuenta de que ya estaba. Cerca del final de la noche, decides ordenar
alfabéticamente la playlist para que sea más fácil de leer, y luego prefieres invertir ese orden
para que las canciones aparezcan de la Z a la A. Finalmente, quieres saber cuántas
canciones quedaron en total, y decides quitar la canción que quedó en la primera posición
porque ya se repitió antes.
Implementa la función:
gestionar_playlist(playlist) que reciba la lista inicial de canciones y devuelva una
lista con: [respaldo, cancion_retirada, posicion_encontrada,
veces_repetida, total_canciones, playlist_final].
Restricción: no uses slicing, +, +=, sorted() ni bucles manuales para lograr lo descrito;
usa exclusivamente los métodos nativos correspondientes a cada acción del relato.
'''

def gestionar_playlist(playlist):
    respaldo = playlist.copy()
    playlist.append("Musa - Soda Stereo")
    
    canciones_amigo = ["Crimen - Cerati", "De Música Ligera - Soda Stereo"]
    playlist.extend(canciones_amigo)
    
    playlist.insert(0, "Arrancamuelas - Wos")
    
    playlist.remove("Arrancamuelas - Wos")
    
    cancion_retirada = playlist.pop(0)

    posicion_encontrada = playlist.index("De Música Ligera - Soda Stereo")

    veces_repetida = playlist.count("De Música Ligera - Soda Stereo")
    
    playlist.sort()
    
    playlist.reverse()
    
    total_canciones = len(playlist)
    
    playlist.pop(0)
    
    playlist_final = playlist

    

    return [respaldo, cancion_retirada, posicion_encontrada, veces_repetida, total_canciones, playlist_final]


playlist_inicial = [
    "De Música Ligera - Soda Stereo", 
    "Mil horas - Los Abuelos de la Nada", 
    "Ji ji ji - Patricio Rey"
]

resultado = gestionar_playlist(playlist_inicial)

print("1. Respaldo inicial:", resultado[0])
print("2. Canción retirada al sonar:", resultado[1])
print("3. Posición encontrada:", resultado[2])
print("4. Veces repetida:", resultado[3])
print("5. Total antes de quitar la repetida:", resultado[4])
print("6. Playlist final:", resultado[5])
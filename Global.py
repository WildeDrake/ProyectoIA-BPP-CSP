""" Parametros Que se pueden modificar """
WIDTH, HEIGHT = 1920, 1080  # tamaño de la pantalla.
dimContenedor = 14, 14    # tamaño de la contenedor.
randConj = 1        # 0 para seed aleatoria, otro para fijar la seed en ese valor.


""" Parametros que no se deben modificar """
area = dimContenedor[0]*dimContenedor[1]  # area del contenedor.

if min(WIDTH, HEIGHT) == WIDTH:
    if min(dimContenedor[0], dimContenedor[1]) == dimContenedor[0]:
        tamCasillas = WIDTH//(dimContenedor[1]*2) + 1
    else:
        tamCasillas = (WIDTH//(dimContenedor[0]*2)) + 1
else:
    if min(dimContenedor[0], dimContenedor[1]) == dimContenedor[0]:
        tamCasillas = (HEIGHT//(dimContenedor[1]*1.1)) + 1
    else:
        tamCasillas = (HEIGHT//(dimContenedor[0]*1.1)) + 1

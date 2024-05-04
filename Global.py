WIDTH, HEIGHT = 1800, 1000  # tamaño de la pantalla.
dimContenedor = 100, 100    # tamaño de la contenedor.
tmno_cuad = 20  # tamaño en pixeles de las cuadriculas.
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
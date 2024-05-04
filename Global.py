WIDTH, HEIGHT = 1000, 1000  # tamaño de la pantalla.
dimContenedor = 100, 100    # tamaño de la contenedor.
tmno_cuad = 20  # tamaño en pixeles de las cuadriculas.
tamCasillas = min([WIDTH // (dimContenedor[0] * 2) + 1,
                   (HEIGHT // (dimContenedor[1] * 1.1)) + 1])
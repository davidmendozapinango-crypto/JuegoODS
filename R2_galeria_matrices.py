import numpy as np #Parte de: Albert

def main():
    ###################################################################################################
    #FALARIA VALIDAR BIEN C/, HACER UNA FUNCION PARA CADA PAREJA Y UN SUB-MENU PARA ELEJIR LA PAREJA SEGUN LA LETRA(SOS)
    ###################################################################################################
    
    #Validacion y Entrada de Datos
    N = int(input("Ingrese la cantidad de filas y columnas de la matriz: "))
    while (N%2 == 0) or (N < 5):
        if (N < 5):
            print("Error, el tamaño debe ser mayor o igual a 5")
        else:
            print("Error, el tamaño debe ser impar")
        N = int(input("Ingrese la cantidad de filas y columnas de la matriz: "))
    print()
            
    #Llenado & Patrones de las Parejas de Matrices 
    #---------------------------------- RELOJES DE ARENA A ----------------------------------
    #Llenado por filas de anajo a arriba de izq a der
    print("A1 - Fin Pobreza")
    reloj_fil = np.zeros((N, N), dtype = "int")
    cont = 1
    centro = N//2
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if i <= centro and j >= i and j <= N-i-1:
                reloj_fil[i][j] = cont
                cont += 1
            elif i >= centro and j <= i and j >= N-i-1:
                reloj_fil[i][j] = cont
                cont += 1
    print(reloj_fil)
    print()
    
    #Llenado de reloj por columnas inverso de abajo a arriba de der a izq
    print("A2 - Hambre Cero")
    reloj_col_inv = np.zeros((N, N), dtype = "int")
    cont = 1
    for j in range(N-1,-1,-1):
        for i in range(N-1,-1,-1):
            if (j <= centro) and (i >= j) and (j <= N-1-i):
                reloj_col_inv[i, j] = cont
                cont += 1
            elif (j >= centro) and (j >= i) and (j >= N-i-1):
                reloj_col_inv[i, j] = cont
                cont += 1
    print(reloj_col_inv)
    print()

    
    #---------------------------------- RELOJES DE ARENA B ----------------------------------
    #Llenado de reloj por columnas inverso de abajo a arriba de der a izq
    print("B1 - Salud y Bienestar")
    reloj_col = np.zeros((N, N), dtype = "int")
    cont = 1
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            if (j <= centro) and (i >= j) and (j <= N-1-i):
                reloj_col[i, j] = cont
                cont += 1
            elif (j >= centro) and (j >= i) and (j >= N-i-1):
                reloj_col[i, j] = cont
                cont += 1
    print(reloj_col)
    print()
    
    #Llenado de reloj por columnas de arriba a abajo de izq a der
    print("B2 - Educacion de Calidad")
    reloj_col = np.zeros((N, N), dtype = "int")
    cont = 1
    #Llenado por columnas
    for j in range(0, N, 1):
        for i in range(0, N, 1):
            if (i <= centro) and (j >= i) and (j <= N - 1 - i):
                reloj_col[i, j] = cont
                cont += 1
            elif (i > centro) and (j >= N - 1 - i) and (j <= i):
                reloj_col[i, j] = cont
                cont += 1
    print(reloj_col, "\n")
    
    
    #---------------------------------- ESQUINAS ----------------------------------
    #Llenado en rombo por filas de abajo a arriba y de der a izq
    print("C1 - Igualdad de Genero")
    rombo_filas = np.zeros((N, N), dtype = "int")
    cont = 1
    med = N//2
    aux = 0
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if i >= med:
                if (j >= med - aux) and (j <= med + aux):
                    rombo_filas[i][j] = cont
                    cont += 1
            elif i < med:
                if (j >= med - i) and (j <= med + i):
                    rombo_filas[i][j] = cont
                    cont += 1
        if i > med:
            aux += 1
    print(rombo_filas)
    print()
    
    #Llenado en rombo por columnas de izq a der y de abajo hacia arriba 
    print("C2 - Agua Limpia y Saneamiento")
    rombo_cols = np.zeros((N, N), dtype = "int")
    cont = 1
    med = N//2
    aux = 0
    for j in range(N-1, -1, -1):
        for i in range(N-1, -1, -1):
            if j >= med:
                if (i >= j - med) and (i <= med + aux):
                    rombo_cols[i][j] = cont
                    cont += 1
            elif j < med:
                if (i >= med - j) and (i <= med + j):
                    rombo_cols[i][j] = cont
                    cont += 1
        if j > med:
            aux += 1
    print(rombo_cols)
    print()
    
    
    #---------------------------------- ROMBOS ----------------------------------
    #Llenado en rombo por filas de abajo a rriba y de der a izq
    print("D1 - Energia Asequible y No Contaminante")
    corners_filas = np.zeros((N, N), dtype = "int")
    cont = 1
    med = N//2
    aux = med
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            if i < med:
                if (j < med - i) or (j >= med + i + 1):
                    corners_filas[i][j] = cont
                    cont += 1
            elif i > med:
                if (j <= med - aux) or (j >= med + aux):
                    corners_filas[i][j] = cont
                    cont += 1
        if i > med:
            aux = aux - 1
    print(corners_filas)
    print()
    
    #Llenado en rombo por columnas de arriba a abajo y de izq a der
    print("D2 - Trabajo Decente y Crecimiento Economico")
    corners_cols = np.zeros((N, N), dtype = "int")
    cont = 1
    med = N//2
    aux = med-1
    for j in range(0, N, 1):
        for i in range(0, N, 1):
            if j < med:
                if (i < med - j) or (i > med + j):
                    corners_cols[i][j] = cont
                    cont += 1
            elif j > med:
                if (i < j - med) or (i > med + aux):
                    corners_cols[i][j] = cont
                    cont += 1
        if j > med:
            aux -= 1
    print(corners_cols)
    print()
    
    
    #---------------------------------- TORNADOS ----------------------------------
    #Llenado en Tornado dejando espacios de recorrido Der->Abajo->Izq->Arriba
    print("E1 - Industria, Innovacion e Infraestructura")
    m_tornado_1 = np.zeros((N, N), dtype=int)
    top = 0
    bottom = N - 1
    left = 0
    right = N - 1
    cont = 1
    while top <= bottom and left <= right:
        #Izquierda a Derecha
        for j in range(left, right + 1):
            if (top + j) % 2 == 0:
                m_tornado_1[top][j] = cont
                cont += 1
        top += 1
        
        #Arriba a Abajo
        for i in range(top, bottom + 1):
            if (i + right) % 2 == 0:
                m_tornado_1[i][right] = cont
                cont += 1
        right -= 1
        
        if top <= bottom:
            #Derecha a Izquierda
            for j in range(right, left - 1, -1):
                if (bottom + j) % 2 == 0:
                    m_tornado_1[bottom][j] = cont
                    cont += 1
            bottom -= 1
            
        if left <= right:
            #Abajo a Arriba
            for i in range(bottom, top - 1, -1):
                if (i + left) % 2 == 0:
                    m_tornado_1[i][left] = cont
                    cont += 1
            left += 1
    print(m_tornado_1)
    print()
    
    #Llenado en Tornado dejando espacios de recorrido Abajo->Der->Arriba->Izq
    print("E2 - Reduccion de las Desigualdades")
    m_tornado_2 = np.zeros((N, N), dtype=int)
    top = 0
    bottom = N - 1
    left = 0
    right = N - 1
    cont = 1
    while top <= bottom and left <= right:
        
        #Arriba a Abajo
        for i in range(top, bottom + 1):
            if (i + left) % 2 == 0:
                m_tornado_2[i][left] = cont
                cont += 1
        left += 1
        
        #Izquierda a Derecha
        for j in range(left, right + 1):
            if (bottom + j) % 2 == 0:
                m_tornado_2[bottom][j] = cont
                cont += 1
        bottom -= 1
        
        #Abajo a Arriba
        if left <= right:
            for i in range(bottom, top - 1, -1):
                if (i + right) % 2 == 0:
                    m_tornado_2[i][right] = cont
                    cont += 1
            right -= 1
            
        #Derecha a Izquierda
        if top <= bottom:
            for j in range(right, left - 1, -1):
                if (top + j) % 2 == 0:
                    m_tornado_2[top][j] = cont
                    cont += 1
            top += 1       
    print(m_tornado_2)
    print()
    
    
    #---------------------------------- DIAGONALES ESPACIADAS ----------------------------------
    #Llenado de diagonales por columas de izq a der de arriba a abajo
    print("F1 - Cudades y Comunidades Sostenibles")
    suma = 0
    diag_top = np.zeros((N, N), dtype=int)
    cont = 1
    for k in range(0, N, 1):
        for j in range(0, N, 1):
            for i in range(0, N, 1):
                if i + j == suma:
                    diag_top[i][j] = cont
                    cont += 1
        suma += 2
    print(diag_top)
    print()
    
    #Llenado de diagonales por columas de izq a der de abajo a arriba
    print("F2 - Produccion y Consumo Responsables")
    suma = N-1
    diag_low = np.zeros((N, N), dtype=int)
    cont = 1
    for k in range(0, N, 1):
        for j in range(0, N, 1):
            for i in range(N-1,-1,-1):
                if i - j == suma:
                    diag_low[i][j] = cont
                    cont += 1
        suma -= 2
    print(diag_low)
    print()
    
    
    #---------------------------------- Z y N ----------------------------------
    #Llenado en Z por filas de abajo a arriba y de der a izq
    print("G1 - Accion por el Clima")  
    zeta = np.zeros((N,N), dtype = "int")
    cont = 1
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if (i == N-1) or (i == 0) or (i+j == N-1):
                zeta[i][j] = cont
                cont += 1
    print(zeta)
    print()
    
    #Llenado en N por columnas de abajo a arriba y de der a izq
    print("G2 - Vida Submarina")  
    ene = np.zeros((N,N), dtype = "int")
    cont = 1
    for j in range(N-1,-1,-1):
        for i in range(N-1,-1,-1):
            if (j == N-1) or (j == 0) or (i+j == N-1):
                ene[i][j] = cont
                cont += 1
    print(ene)
    print()
    
    
    #---------------------------------- DIAGONALES SIN CENTRO ----------------------------------
    #Llenado de diagonales sin centro por filas de abajo a arriba en ambos sentidos
    print("H1 - Vida de Ecosistemas Terrestres")
    diag = np.zeros((N,N), dtype = "int")
    cont = 1
    for j in range(0, N, 1):
        for i in range(N-1, -1, -1):
            if i + j == N-1 and i != j:
                diag[i][j] = cont
                cont += 1               
    for j in range(N-1, -1, -1):
        for i in range(N-1, -1, -1):
            if i == j and i != N//2:
                diag[i][j] = cont
                cont += 1
    print(diag)
    print()
    
    #Llenado de diagonales sin centro por filas de abajo a arriba en ambos sentidos
    print("H2 - Paz, Justicia e Instituciones Solidas")
    diag_inv = np.zeros((N,N), dtype = "int")
    cont = 1
    for j in range(N-1, -1, -1):
        for i in range(N-1, -1, -1):
            if i == j and i != N//2:
                diag_inv[i][j] = cont
                cont += 1
    for j in range(0, N, 1):
        for i in range(N-1, -1, -1):
            if i + j == N-1 and i != j:
                diag_inv[i][j] = cont
                cont += 1
    print(diag_inv)
    print()

     
if __name__ == "__main__":      
    main()
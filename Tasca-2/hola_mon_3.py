def main():#he pujat a la linea 1 
    #inici programa
    print ( 'HOLA MON 3' )  # he posat el print en una linea de codi
    print ( 'Pensa un número del 1 a 4.' )  # he tret espais l'he pujat una linea
    print ( "Contesta S (si) o N (no) a les preguntes." )  # he tret espais

    primera = input( "El número pensat és major de 2? " ) # Res
    if primera == "S": # he tret espais
        segona = input ( "El número pensat és major de 3? ") # He tret espais i tret una tabulacio

        if segona == "S": # he posat les tabulacions en segoona linea i pujarlo dos lineas
            print ( "El número pensat és 4." ) # tabulacions corregides
        else:# he posat en segona linea per esta a l'altura del "if" linea 11 
            print("El número pensat és 3") # tabulacions corregides
    else: # Res esta a la altura del primer if de la linea  8
        segona = input("El número pensat és major de 1? ")# he corregit espais i tabulacions

        if segona == 'S':#he tret els espais i corregit tabulacions
            print("El número pensat és 2.") # Treure espais i tabulacions
        else: # les tabulacions a la altura de l'if de la linea 18
            print("El número pensat és 1.") # # corregir espais i tabulacions 
    print("A reveure!")  # he posat el print en una sola linea


if __name__ == "__main__":

    main()

    #Kevin Gaspar Rubio

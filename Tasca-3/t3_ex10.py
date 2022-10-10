# Arxiu: t2_e10.py
# Autor:Kevin Gaspar Rubio
# Data: 16/09/2022
# Descripció:Exercicis de Variables, Entrada i Sortida i
#            Operacions aritmètiques elementals

def main():
 
    valorUsuari = int(input("Entra un valor numeric: "))
    grosses = int(valorUsuari/144) # calcul de les grosses
    restoGrosses = int(valorUsuari%144) # li donem una variavle a la resto de la div per calcula dotzenes
    dotzenes = int(restoGrosses/12)# calculem les dotzenes sobrans 
    unitats = int(restoGrosses%12)# del resto treurem les unitats
    print(f"Del valor entrat surten {grosses} grosses, {dotzenes} dotzenes i {unitats} unitats.")
    
 
 
if __name__ == "__main__":
    main()
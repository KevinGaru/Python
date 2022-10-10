# Arxiu: t2_e8.py
# Autor:Kevin Gaspar Rubio
# Data: 16/09/2022
# Descripció:Exercicis de Variables, Entrada i Sortida i
#            Operacions aritmètiques elementals

def main():
   #entrada de dades
    segons = float(input("Entra una quantitat de segons: "))

    #calcul i sortida per pantalla
    minuts = int(segons/60)
    segons1 = int(segons%60)
    print(f"Els segons entrats {segons} són tans {minuts} minuts i {segons1} segons.")
 
if __name__ == "__main__":
    main()
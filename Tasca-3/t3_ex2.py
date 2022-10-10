# Arxiu: t2_e2.py
# Autor:Kevin Gaspar Rubio
# Data: 16/09/2022
# Descripció:Exercicis de Variables, Entrada i Sortida i
#            Operacions aritmètiques elementals

def main():
    
 numero1 = float(input("Introdueix el seu pes")) #aqui recollim les dades
 numero2 = float(input("Introdueix l'altura "))

 imc= (numero1 / (numero2**2))
 
 print (f"El seu imc és {imc}")

if __name__ == "__main__":
    main()
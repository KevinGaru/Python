# Arxiu: t2_e3.py
# Autor:Kevin Gaspar Rubio
# Data: 16/09/2022
# Descripció:Exercicis de Variables, Entrada i Sortida i
#            Operacions aritmètiques elementals

def main():
 print("POLZADES, PEU,CM")
 print()
 numero1 = float(input("Introdueix els peus: ")) #aqui recollim les dades
 numero2 = float(input("Introdueix polzades:"))

 #calcul de peu a cm
 centimetre2 = numero1 * 30.48
 centimetre3 = ((numero1*12)*2.54)
 # calcul de polzades a cm
 centimetre1 = numero2 * 2.54

 print (f"La distancia introduida en peus '{numero1}' són {centimetre3}cm")
 print (f"La distancia introduida en peus '{numero1}' són {centimetre2}cm")
 print (f"La distancia introduida en polzades '{numero2}' són {centimetre1}cm")




if __name__ == "__main__":
    main()
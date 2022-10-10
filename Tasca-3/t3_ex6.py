# Arxiu: t2_e6.py
# Autor:Kevin Gaspar Rubio
# Data: 16/09/2022
# Descripció:Exercicis de Variables, Entrada i Sortida i
#            Operacions aritmètiques elementals

def main():
   
   grausC= float (input("Introdueix la temperatura en graus Celsius."))
   fahrenheit= 1.8 * grausC + 32 
   print(f"La temperatura entrada {grausC} són {fahrenheit}f.")
    
if __name__ == "__main__":
    main()
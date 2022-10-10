# Arxiu: t2_e7.py
# Autor:Kevin Gaspar Rubio
# Data: 16/09/2022
# Descripció:Exercicis de Variables, Entrada i Sortida i
#            Operacions aritmètiques elementals
def main():
   #entrada de dades
   fahrenheit= float (input("Introdueix la temperatura en graus fahrenheit."))
   #calcul i resposta
   celsius =(fahrenheit-32)/1.8  
   print(f"La temperatura entrada {fahrenheit} són {celsius}c.")
    
if __name__ == "__main__":
    main()
# Arxiu: t2_e1.py
# Autor:Kevin Gaspar Rubio
# Data: 16/09/2022
# Descripció:Exercicis de Variables, Entrada i Sortida i
#            Operacions aritmètiques elementals

def main():
    print("MITJANA ARITMÈTICA")
    print()
    numero1 = int(input("Escriu el primer nombre ")) #aqui recollim la primera variable
    numero2 = int(input("Escriu el segon nombre "))

    mitjana = (numero1 + numero2) / 2 #calculem la mitjana

    print(f"La mitjana aritmètica és {mitjana}")


if __name__ == "__main__":
    main()
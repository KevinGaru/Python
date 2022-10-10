# Arxiu: t6_e1.py
# Autor:Kevin Gaspar Rubio
# Data: 10/10/2022
# Descripció: Sèntencies condicionals

def main():
 
    numParell = int(input("Entra un valor numeric parell: "))
    numImparell = int(input("Entra un valor numeric imparell: "))
    if numParell % 2 != 0 or numImparell % 2 == 0:
        print("Un o més dels valors que heu escrit no són correctes.")
        print("Executeu de nou el programa per tornar a intentar-ho.")   
    
 
 
if __name__ == "__main__":
    main()
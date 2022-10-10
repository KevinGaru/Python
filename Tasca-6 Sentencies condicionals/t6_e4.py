# Arxiu: t6_e4.py
# Autor:Kevin Gaspar Rubio
# Data: 10/10/2022
# Descripció: Sèntencies condicionals

def main():
 
    numParell = int(input("Entra un valor numeric parell: "))    
    if numParell % 2 != 0:
        print(f"El valor que heu escrit {numParell} no és parell.")
   
    numImparell = int(input("Entra un valor numeric imparell: "))
    if numImparell % 2 == 0:
        print(f"El valor que heu escrit {numImparell} no és imparell. ")
   
 
if __name__ == "__main__":
    main()
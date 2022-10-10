# Arxiu: t6_e3.py
# Autor:Kevin Gaspar Rubio
# Data: 10/10/2022
# Descripció: Sèntencies condicionals

def main():
 
    numParell = int(input("Entra un valor numeric parell: "))
    numImparell = int(input("Entra un valor numeric imparell: "))
    
    if numParell % 2 != 0:
        print(f"El valor que heu escrit {numParell} no és parell.")
    
    if numImparell % 2 == 0:
        print(f"El valor que heu escrit {numImparell} no és imparell. ")
   
 
if __name__ == "__main__":
    main()
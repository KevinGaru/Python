# Arxiu: t6_e2.py
# Autor:Kevin Gaspar Rubio
# Data: 10/10/2022
# Descripció: Sèntencies condicionals

def main():
 
    numParell = int(input("Entra un valor numeric parell: "))
    if numParell % 2 == 0:
        numImparell = int(input("Entra un valor numeric imparell: "))
        if numImparell % 2 == 0:
            print(f"El valor { numImparell}  no és correcte.")
    else:
        print(f"El valor  {numParell} no és correcte.") 
    
if __name__ == "__main__":
    main()
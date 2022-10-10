# Arxiu: t2_e9.py
# Autor:Kevin Gaspar Rubio
# Data: 16/09/2022
# Descripció:Exercicis de Variables, Entrada i Sortida i
#            Operacions aritmètiques elementals

def main():
 
    totalSeg = int(input("Introdueix una quantitat de segons a convertir: "))
    hores = int(totalSeg/3600)# calcul de les hores
    resHores = int(totalSeg%3600)# del'restrola diviso de segons calcularem els minuts
    minuts = int(resHores/60)# calcul de minuts
    segons = int(resHores%60)# fem servir la resto de la divisio per trobar els s
    print(f"Dels {totalSeg}s entrats, surten {hores}h {minuts}m i {segons}s. ")
 
 
if __name__ == "__main__":
    main()
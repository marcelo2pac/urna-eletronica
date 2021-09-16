print("Justiça Eleitoral 2020")
print("Candidato Edivaldo nº 10")
print("Candidato Daniele nº 20")
print("Canditado Rodrigo nº 30")
print("Número do Prefeito: ")



def main():
    
    nE = 0
    nD = 0
    nR = 0
    vN = 0
    
    while True: 
        n = input()
        if n == "10":
            print("Votou em Edvaldo!")
            nE += 1
            print("__")
        elif n == "20":
            print("Votou em Daniele!")
            nD += 1
            print("__")
        elif n == "30":
            print("Votou em Rodrigo!")
            nR += 1
            print("__")
        elif n == "CONT":
            print("Total de votos: ", n)
            print("__")

        elif n == ("Edvaldo"):
            print("Número de votos Edvaldo: ",nE)
        elif n == ("Daniele"):
            print("Número de votos Daniele: ",nD)
        elif n == ("Rodrigo"):
            print("Número de votos Rodrigo: ",nR)

        elif n == ("novoladrao"):
            def resultado():
                if nE > nD and nE > nR:
                    print("Edvaldo é o novo Prefeito com ", nE, " voto(s)!")
                    print("Voto(s) Daniele: ", nD)
                    print("Voto(s) Rodrigo", nR)
                    print("Voto(s) nulo: ", vN)
                elif nD > nE and nD > nR:
                    print("Daniele é o novo Prefeito com ", nD, " voto(s)!")
                    print("Voto(s) Edvaldo: ", nE)
                    print("Voto(s) Rodrigo", nR)
                    print("Voto(s) nulo: ", vN)
                elif nR > nD and nR > nE:
                    print("Rodrigo é o novo Prefeito com ", nR, " voto(s)!")
                    print("Voto(s) Edvaldo: ", nE)
                    print("Voto(s) Daniele: ", nD)
                    print("Voto(s) nulo: ", vN)
                else:
                    print("Empate técnico!!!")
                    print("Voto(s) Edvaldo: ", nE)
                    print("Voto(s) Daniele: ", nD)
                    print("Voto(s) Rodrigo", nR)
                    

            
            print("Votações encerradas!")
            print("****")
            resultado()
            print("OBRIGADO POR VOTAR!")
            input()
            exit()
        else:
            n != ("r") and n != "30" and n != "10" and n !="20"
            print("VOTO NULO!")
            vN += 1
            print("__")
            if n == "NULO":
                print("Votos Nulos: ", vN-1)
        print()
        print("Número do prefeito: ")
    
main()
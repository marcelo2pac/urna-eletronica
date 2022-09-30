print("Justiça Eleitoral 2022")
print("Candidato Lula nº 13")
print("Candidato Bolsonaro nº 17")
print("Canditado Ciro Gomes nº 12")

print("Número do Presidente: ")


def main():

  nL = 0
  nB = 0
  nC = 0
  vN = 0

  while True:
    n = input()
    if n == "13":
      print("Votou em Lula!")
      nL += 1
      print("__")
    elif n == "17":
      print("Votou em Bolsonaro!")
      nB += 1
      print("__")
    elif n == "12":
      print("Votou em Ciro Gomes!")
      nC += 1
      print("__")
    elif n == "CONTAGEM":
      print("Total de votos: ", n)
      print("__")

    elif n == ("Lula"):
      print("Número de votos Lula: ", nL)
    elif n == ("Bolsonaro"):
      print("Número de votos Bolsonaro: ", nB)
    elif n == ("Ciro Gomes"):
      print("Número de votos Ciro Gomes: ", nC)

    elif n == ("novopresidente"):

      def resultado():
        if nL > nB and nL > nC:
          print("Lula é o novo Presidente com ", nL, " voto(s)!")
          print("Voto(s) Bolsonaro: ", nB)
          print("Voto(s) Ciro Gomes", nC)
          print("Voto(s) nulo: ", vN)
        elif nB > nL and nB > nC:
          print("Bolsonaro é o novo Presidente com ", nB, " voto(s)!")
          print("Voto(s) Lula: ", nL)
          print("Voto(s) Ciro Gomes", nC)
          print("Voto(s) nulo: ", vN)
        elif nC > nB and nC > nL:
          print("Ciro Gomes é o novo Presidente com ", nC, " voto(s)!")
          print("Voto(s) Lula: ", nL)
          print("Voto(s) Bolsonaro: ", nB)
          print("Voto(s) nulo: ", vN)
        else:
          print("Empate técnico!!!")
          print("Voto(s) Lula: ", nL)
          print("Voto(s) Bolsonaro: ", nB)
          print("Voto(s) Ciro Gomes", nC)

      print("Votações encerradas!")
      print("****")
      resultado()
      print("OBRIGADO POR VOTAR!")
      input()
      exit()
    else:
      n != ("c") and n != "12" and n != "13" and n != "17"
      print("VOTO NULO!")
      vN += 1
      print("__")
      if n == "NULO":
        print("Votos Nulos: ", vN - 1)
    print()
    print("Número do Presidente: ")


main()
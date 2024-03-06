import random

class Domanda:
    def __init__(self, testo, livello, risposta_corretta, risposte_errate):
        self.testo = testo
        self.livello = livello
        self.risposta_corretta = risposta_corretta
        self.risposte_errate = risposte_errate

def carica_domande(file):
    domande = []
    with open(file, 'r') as f:
        righe = f.readlines()
        i = 0
        while i < len(righe):
            testo = righe[i].strip()
            livello = int(righe[i+1].strip())
            risposta_corretta = righe[i+2].strip()
            risposte_errate = [righe[i+3].strip(), righe[i+4].strip(), righe[i+5].strip()]
            domanda = Domanda(testo, livello, risposta_corretta, risposte_errate)
            domande.append(domanda)
            i += 7
    return domande

def main():
    domande = carica_domande("domande.txt")
    random.shuffle(domande)

    punteggio = 0
    livello_corrente = 0

    while livello_corrente < len(domande):
        domanda_corrente = None
        for domanda in domande:
            if domanda.livello == livello_corrente:
                domanda_corrente = domanda
                break

        if domanda_corrente is not None:
            print(f"\nLivello {livello_corrente}) {domanda_corrente.testo}?")
            risposte = [domanda_corrente.risposta_corretta] + domanda_corrente.risposte_errate
            random.shuffle(risposte)
            for i, risposta in enumerate(risposte):
                print(f"\t{i + 1}. {risposta}")
            risposta_utente = input("Inserisci la risposta: ").strip()
            if risposta_utente == str(risposte.index(domanda_corrente.risposta_corretta) + 1):
                print("Risposta corretta!")
                punteggio += 1
                livello_corrente += 1
            else:
                print(f"Risposta sbagliata! La risposta corretta era: {risposte.index(domanda_corrente.risposta_corretta) + 1}")
                break

    print(f'\nHai totalizzato {punteggio} punti!')
    nickname = input("Inserisci il tuo nickname: ")

    with open("punti.txt", "a") as f:
        f.write(f"{nickname} {punteggio}\n")

    # Ordina il file punti.txt in ordine decrescente di punteggio
    with open("punti.txt", "r+") as f:
        righe = f.readlines()
        righe.sort(key=lambda x: int(x.split()[1]), reverse=True)
        f.seek(0)
        f.truncate()
        f.writelines(righe)

if __name__ == "__main__":
    main()

# SPIEGAZIONE

_traduttore_ENG_to_ITA_csv.py_ permette di tradurre tutti i file csv presenti nella stessa cartella del .py ed inserire l'output nella cartella "tradotto". <br>
Alcuni file csv hanno una struttura differenti, quello che interessa è la _c_lettura_ e _c_scrittura_. La c_scrittura corrisponde alla colonna di output della traduzione (tendenzialmente l'ultima), la c_lettura è la colonna dove è presente il testo originale in inglese.

Ovviamente la traduzione non sempre è perfetta, alcune parole vengono tradotte per errore (come alcuni nomi), la formatazzione non sempre è corretta ed alcuni caratteri non sono letti correttamente.

## CARATTERI PARTICOLARI

Tutte le lettere accentate non sono supportate dal font originale del gioco, la patch francese modifica il font originale per supportare anche questi caratteri ma non tutti quelli utilizzati anche nella lingua italiana. I caratteri vengono sostituiti da altri nel testo.<br>

Allo stato attuale i caratteri supportati sono:
```
< --> é
> --> è
= --> à
```
Il resto viene modificato con l'aggiunta di " _'_ ".

## LUNGHEZZA MASSIMA

Da cosa ho potuto comprendere il carattere "_&_", ha la stessa funzione del "_\n_". Il carattere per andare a capo, deve essere inserito prima dei 60 caratteri, in caso contrario, la visualizzazione del testo in gioco risulterà errata. Per questo il codice per le stringhe sotto i 120 caratteri (le stringhe che superano i 120 caratteri sono ancora da analizzare), inserisce al 59 carattere il simbolo "_-_" e al 60 "_&_". Questa suddivisione non è ottimale, in quanto la suddivisione non è seguendo la sillabazione italiana. Quindi va comunque rivista e corretta scegliendo di sistemare la suddivisione oppure spostare la parola nell'altra riga.


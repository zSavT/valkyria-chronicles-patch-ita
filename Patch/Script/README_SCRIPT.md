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


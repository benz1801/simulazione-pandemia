# Simulazione di Pandemia

## Descrizione
Questo progetto è una simulazione di una pandemia implementata in Python utilizzando il modulo `turtle` per visualizzare l'evoluzione della malattia in una popolazione virtuale. Ogni individuo nella simulazione è rappresentato da una "tartaruga" che si muove casualmente in un'area definita.

## Requisiti
- Python 3.x
- Modulo `turtle` (incluso di default in Python)

## Installazione
1. Clona il repository:
    ```bash
    git clone https://github.com/benz1801/simulazione-pandemia.git
    ```
2. Entra nella directory del progetto:
    ```bash
    cd simulazione-pandemia
    ```
3. Esegui il programma:
    ```bash
    python simulazione_pandemia.py
    ```

## Utilizzo
Il programma esegue una simulazione basata sui parametri specificati. Gli utenti possono modificare i seguenti parametri nella funzione `simulazione`:

- `r`: Raggio dell'area di simulazione (in pixel).
- `n`: Numero di individui nella simulazione.
- `p`: Probabilità che un individuo sia infetto all'inizio della simulazione.
- `d`: Distanziamento sociale.
- `v`: Movimenti giornalieri degli individui.
- `g`: Numero di giorni da simulare.
- `c`: Raggio di contagio.
- `h`: Durata della malattia.
- `m`: Tasso di mortalità giornaliero.

### Esempio di Esecuzione
```python
simulazione(r=300, n=100, p=0.2, d=10, v=20, g=50, c=10, h=15,m=0.05)

# Simulazione di Pandemia

## Descrizione
Questo progetto è una simulazione di una pandemia implementata in Python utilizzando il modulo `turtle` per visualizzare l'evoluzione della malattia in una popolazione virtuale. Ogni individuo nella simulazione è rappresentato da una "tartaruga" che si muove casualmente in un'area definita.

## Requisiti
- Python 3.x
- Modulo `turtle` (incluso di default in Python)

## Installazione
1. Clona il repository:
    ```bash
    git clone https://github.com/tuo-username/simulazione-pandemia.git
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

- `n`: Numero di individui nella simulazione.
- `r`: Raggio dell'area di simulazione (in pixel).
- `p`: Probabilità che un individuo sia infetto all'inizio della simulazione.
- `g`: Numero di giorni da simulare.
- `m`: Probabilità che un individuo infetto muoia durante la simulazione.

### Esempio di Esecuzione
```python
simulazione(n=100, r=300, p=0.2, g=50, m=0.05, h=..., v=..., c=..., d=...)

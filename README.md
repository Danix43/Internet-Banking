# Internet Banking GUI App

Această aplicație este o simulare simplificată de internet banking cu interfață grafică, creată folosind biblioteca [Dear PyGui](https://github.com/hoffstadt/dearpygui). Permite autentificarea utilizatorilor, vizualizarea soldului și a tranzacțiilor, trimiterea de bani între conturi și înregistrarea de noi utilizatori.

## Funcționalități

- Autentificare cu nume de utilizator și parolă
- Înregistrare cont nou cu sold inițial
- Vizualizare detalii cont: IBAN, sold, nume utilizator
- Tranzacții bancare între utilizatori existenți
- Istoric tranzacții pentru fiecare cont
- Salvarea conturilor si detaliilor lor

## Structura proiectului

```
├── Bank.py           # Conține logica de bază: clasele Bank, User, Transaction
├── main.py           # Aplicația cu interfață grafică
```

## Cerințe

- Python 3.7+
- dearpygui

Instalare dependințe:

```bash
pip install dearpygui
```

## Rulare

```bash
python main.py
```

## Exemple de utilizare

1. Pornește aplicația și autentifică-te cu:
   - username: `user1`
   - password: `password`

2. Vizualizează soldul și tranzacțiile curente.
3. Folosește meniul „Send Money” pentru a efectua transferuri.
4. Deconectează-te și înregistrează un cont nou folosind meniul „Register”.

## Dezvoltatori

- Acest proiect a fost realizat pentru scopuri educaționale și demonstrează funcționalități de bază ale unui sistem bancar GUI.

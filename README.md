## Wymagania

Aby uruchomić testy lokalnie, upewnij się, że masz zainstalowane poniższe oprogramowanie:
- Python 3.9+
- pip

Dodatkowo, będziemy używać następujących zależności:

- Playwright
- Pytest
- pytest-xdist

## Instalacja zależności 

Po pobraniu projektu zainstaluj wymagane zależności za pomocą pip:
   ```
   pip install -r requirements.txt
   ```

### Uruchamianie testów
Testy możesz uruchomić za pomocą pytest. 
Test jest uruchamiany w 3 sparametryzowanych przeglądarkach równocześnie
   ```
   pytest -n 3  
   ```

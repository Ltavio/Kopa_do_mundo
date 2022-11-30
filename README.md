# Kopa do Mundo

## Como rodar os testes localmente

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```

4. Rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```



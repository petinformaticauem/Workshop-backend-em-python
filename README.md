Como executar esse programa:

1° criar um ambiente virtual usando venv:
  - WINDOWS: Na pasta raiz desse projeto (/work-shop-backend-em-python) digite o comando no terminal: "python -m venv venv" e sempre que for usar o ambiente virtual, digite: "venv\Scripts\activate"
  - LINUX / MacOS: Na pasta raiz desse projeto (/work-shop-backend-em-python) digite o comando no terminal: "python3 -m venv venv" e sempre que for usar o ambiente virtual, digite: "source venv/bin/activate"

2° Instalar os requerimentos:
  - Na pasta raiz desse projeto (/work-shop-backend-em-python) digite o comando no terminal: "pip install -r ./requirements.txt" (tem q ter o pip instalado)

3° Rodar o fastAPI:
  - Na pasta backend desse projeto (/work-shop-backend-em-python/backend)  digite o comando no terminal: "poetry run uvicorn main:app --reload" e acesse "http://127.0.0.1:8000/docs" pelo navegador 

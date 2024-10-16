Como executar esse programa:
1° criar um ambiente virtual usando venv:
  - Na pasta raiz desse projeto (/work-shop-backend-em-python) digite o comando no terminal: "py -m venv venv", se for windows

2° Instalar os requerimentos:
  - Na pasta raiz desse projeto (/work-shop-backend-em-python) digite o comando no terminal: "pip install -r ./requirements.txt" (tem q ter o pip instalado)

3° Rodar o fastAPI:
  - Na pasta backend desse projeto (/work-shop-backend-em-python/backend)  digite o comando no terminal: "poetry run uvicorn main:app --reload" e acesse "http://127.0.0.1:8000/docs" pelo navegador 

# Лабораторная работа 1: HTTP-сервер

## Запуск локально
pip install fastapi uvicorn
uvicorn main:app --reload

## Запуск в Docker
docker compose up --build

## Endpoints
- GET / — приветствие
- GET /health — проверка работоспособности
- GET /info — информация о HTTP-запросе
- GET /docs — автодокументация Swagger

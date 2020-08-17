[![Python version](https://img.shields.io/badge/Python-3.7-green)](https://www.python.org/)
[![Fastapi version](https://img.shields.io/badge/fastapi-0.60.1-green)](https://www.python.org/)
[![Aiofiles version](https://img.shields.io/badge/aiofiles-0.5.0-green)](https://www.python.org/)
[![GitHub issues][issues-shield]][issues-url]
![GitHub repo size](https://img.shields.io/github/languages/code-size/dmitrii1991/fastapi_server)
![GitHub last commit](https://img.shields.io/github/last-commit/dmitrii1991/fastapi_server)
[![GitHub stars][stars-shield]][stars-url]

# Server for storing files

## Description
Простой сервер для загрузки/хранения/удаления файлов первая реализация

Переименуйте docker-compose-template.yml в docker-compose.yml


##  Run
```shell script
docker-compose up
```

## API documentation
* http://127.0.0.1:80/docs
* http://127.0.0.1:80/redoc

## For the future
* authentication
* encryption

### some  API methods
### File
- [x] POST **/file/upload/**
- [X] GET **/file/status/**
```cmd
curl -X GET "http://127.0.0.1:80/file/status/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"full_name\":\"example_file\"}"
```
- [X] GET **/file/download/{filename}**
```cmd
curl -X GET "http://127.0.0.1:80/file/download/example_file" -H  "accept: application/json"
```
- [x] DELETE **/file/delete/{filename}**
```cmd
curl -X DELETE "http://127.0.0.1:80/file/delete/example_file" -H  "accept: application/json"
```


[stars-shield]: https://img.shields.io/github/stars/dmitrii1991/fastapi_server?style=social
[stars-url]: https://github.com/dmitrii1991/fastapi_server/stargazers

[issues-shield]: https://img.shields.io/github/issues/dmitrii1991/fastapi_server
[issues-url]: https://github.com/dmitrii1991/fastapi_server/issues



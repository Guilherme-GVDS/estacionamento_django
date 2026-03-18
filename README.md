# 🅿️ Parking Service

Sistema de gerenciamento de estacionamento desenvolvido com Django e Django REST Framework, com painel administrativo, API RESTful, autenticação JWT e containerização via Docker.

---

## 📋 Funcionalidades

- Painel administrativo com Jazzmin
- API RESTful com autenticação JWT
- Cadastro de clientes, veículos, vagas e registros de entrada/saída
- Status de vagas atualizado automaticamente via signals
- Filtros avançados com RQL
- Documentação da API com Swagger e Redoc
- Permissões diferenciadas entre admin, funcionário e cliente
- Containerização com Docker e Docker Compose

---

## 🛠️ Tecnologias

- **Python 3.13**
- **Django 6.0**
- **Django REST Framework**
- **PostgreSQL 15**
- **Docker / Docker Compose**
- **JWT** — `djangorestframework-simplejwt`
- **RQL** — `dj-rql`
- **Swagger** — `drf-spectacular`
- **Jazzmin** — tema para o Django Admin
- **python-decouple** — gerenciamento de variáveis de ambiente

---

## 🚀 Como rodar o projeto

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/estacionamento_django.git
cd estacionamento_django
```

### 2. Configure as variáveis de ambiente

Copie o arquivo de exemplo e preencha com seus dados:

```bash
cp .env.example .env
```

Edite o `.env`:

```env
SECRET_KEY=sua_secret_key_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=parking_service
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=parking_db
DB_PORT=5432
```

### 3. Suba os containers

```bash
docker-compose up --build
```

O servidor estará disponível em: `http://localhost:8000`

### 4. Crie o superusuário

Em outro terminal, com os containers rodando:

```bash
docker-compose exec parking_service python manage.py createsuperuser
```

---

## 📚 Documentação da API

| Interface | URL |
|-----------|-----|
| Swagger | `http://localhost:8000/api/v1/docs/` |
| Redoc | `http://localhost:8000/api/v1/redoc/` |
| Schema | `http://localhost:8000/api/v1/schema/` |

---

## 🔐 Autenticação

A API utiliza JWT. Para obter o token:

```http
POST /api/v1/authentication/token/
Content-Type: application/json

{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Use o token retornado no header das requisições:

```http
Authorization: Bearer <seu_token>
```

---

## 📡 Endpoints

| Recurso | Endpoint |
|---------|----------|
| Clientes | `/api/v1/customers/` |
| Veículos | `/api/v1/vehicles/` |
| Tipos de veículo | `/api/v1/vehicles/types/` |
| Marcas | `/api/v1/vehicles/brands/` |
| Modelos | `/api/v1/vehicles/models/` |
| Cores | `/api/v1/vehicles/colors/` |
| Vagas | `/api/v1/parking/spots/` |
| Registros | `/api/v1/parking/records/` |
| Token | `/api/v1/authentication/token/` |
| Refresh | `/api/v1/authentication/token/refresh/` |
| Verify | `/api/v1/authentication/token/verify/` |

---

## 🗂️ Estrutura do Projeto

```
estacionamento_django/
├── authentication/       # Configuração de autenticação JWT
├── core/                 # Settings, URLs e permissões globais
├── customers/            # App de clientes
├── vehicles/             # App de veículos (marca, modelo, cor, tipo)
├── parking/              # App de vagas e registros
├── static/               # Arquivos estáticos (logo, etc.)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

---

## 🔑 Exemplo de Perfis de Acesso

| Perfil | Acesso |
|--------|--------|
| **Admin** | Acesso total à API, ao painel administrativo e gerenciamento de usuários |
| **Funcionário** | Cadastra e edita clientes e veículos, além de criar e alterar registros de estacionamento. Não possui acesso ao painel administrativo nem ao gerenciamento de usuários |
| **Cliente** | Visualiza apenas seus próprios veículos e registros de estacionamento via API |

---

## 🧑‍💻 Painel Administrativo

Acesse em: `http://localhost:8000/`

Login com o superusuário criado anteriormente.

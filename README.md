# 🅿️ Parking Service

Sistema de gerenciamento de estacionamento desenvolvido com Django e Django REST Framework. O Django Admin é utilizado como **backoffice** para operações internas, com API RESTful, autenticação JWT e containerização via Docker.

> ⚠️ **Este projeto é um MVP (Minimum Viable Product).** A estrutura atual atende aos requisitos essenciais de operação, com espaço planejado para evoluções futuras descritas ao final deste documento.

---

## 📋 Funcionalidades

- Backoffice administrativo com Django Admin (tema Jazzmin)
- API RESTful com autenticação JWT
- Cadastro de clientes, veículos, vagas e registros de entrada/saída
- Status de vagas atualizado automaticamente via Django Signals
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
- **Whitenoise** — servir arquivos estáticos em produção
- **python-decouple** — gerenciamento de variáveis de ambiente

---

## 🏗️ Arquitetura

O projeto é dividido em quatro apps Django principais:

- **`authentication`** — configuração de autenticação JWT
- **`customers`** — gerenciamento de clientes
- **`vehicles`** — gerenciamento de veículos, marcas, modelos, cores e tipos
- **`parking`** — gerenciamento de vagas e registros de entrada/saída

O **Django Admin** funciona como backoffice, sendo a interface principal para operadores e administradores gerenciarem os dados do sistema. O controle de ocupação das vagas é feito automaticamente via **Django Signals**: ao salvar um `ParkingRecord`, o status da vaga é atualizado de acordo com a presença ou ausência de `exit_time`.

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
CSRF_TRUSTED_ORIGINS=https://seu-dominio.com
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
├── static/               # Arquivos estáticos (logo, CSS customizado, etc.)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

---

## 🔑 Perfis de Acesso

| Perfil | Acesso |
|--------|--------|
| **Admin** | Acesso total à API, ao backoffice (Django Admin) e gerenciamento de usuários |
| **Funcionário** | Cadastra e edita clientes e veículos, cria e altera registros de estacionamento. Sem acesso ao Django Admin nem ao gerenciamento de usuários |
| **Cliente** | Visualiza apenas seus próprios veículos e registros de estacionamento via API |

---

## 🧑‍💻 Backoffice (Django Admin)

Acesse em: `http://localhost:8000/`

O Django Admin é utilizado como interface de backoffice para operadores e administradores. Através dele é possível gerenciar todos os recursos do sistema, incluindo clientes, veículos, vagas e registros, com filtros, buscas e controle de permissões por grupo de usuário.

---

## 🔭 Melhorias Planejadas (Pós-MVP)

### Autopreenchimento de veículos via API de placas

Atualmente, o cadastro de veículos exige o preenchimento manual de marca, modelo e cor. Uma melhoria planejada é a integração com uma API externa de consulta de placas (ex: [FIPE](https://deividfortuna.github.io/fipe/) ou similares), que retornaria automaticamente essas informações a partir da placa informada.

Para não impactar o tempo de resposta da API durante o cadastro, essa integração seria implementada de forma assíncrona utilizando **Celery** com um broker de mensagens (ex: Redis). O fluxo seria:

1. O veículo é cadastrado com apenas a placa
2. A API retorna imediatamente com sucesso
3. Uma task Celery é enfileirada em background
4. A task consulta a API de placas e atualiza os campos `brand`, `model` e `color` no banco de dados automaticamente

Isso garante que o uso da API não seja afetado pela latência de serviços externos.

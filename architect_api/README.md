# Architect API

A FastAPI service for the Architect project.

## Setup

1. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Install dependencies:
```bash
uv sync
```

## Running the Service

### Development
```bash
uv run python main.py
```

### Production
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## Development

### Running tests
```bash
uv run pytest
```

### Adding new dependencies
```bash
uv add package-name
```

### Adding development dependencies
```bash
uv add --dev package-name
```

## API Endpoints

- `GET /` - Welcome message
- `GET /api/v1/hello/` - Hello World endpoint
- `GET /api/v1/hello/{name}` - Personalized hello endpoint

## Interactive Documentation

Once the service is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 
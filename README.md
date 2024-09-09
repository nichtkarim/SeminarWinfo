# Podman WebApp Projekt

Dieses Projekt demonstriert die Verwendung von Podman zur Containerisierung einer Python-API, einer Webanwendung und einer PostgreSQL-Datenbank sowie die Bereitstellung der HTML-Seite mit einem Apache-Webserver.

## Anforderungen

- Podman
- Python 3
- PostgreSQL

## Setup

### 1. PostgreSQL Container starten

```bash
podman run --name postgres-db -e POSTGRES_PASSWORD=mysecretpassword -d docker.io/library/postgres
```

### 2. Python API Container starten

```bash
podman run --name python-api -p 5000:5000 -v $(pwd):/app -w /app python:3.9-alpine sh -c "pip install Flask psycopg2-binary && python app.py"
```

### 3. Apache-Webserver starten

```bash
podman run --name apache-web -p 8080:80 -v $(pwd)/index.html:/usr/local/apache2/htdocs/index.html:ro -d docker.io/library/httpd
```

### 4. Webanwendung im Browser anzeigen

Öffne deinen Browser und gehe zu `http://localhost:8080`, um die statische HTML-Seite anzuzeigen.

### 5. API im Browser anzeigen

Öffne deinen Browser und gehe zu `http://localhost:5000`, um die dynamischen Daten der API zu sehen.

## Container stoppen

```bash
podman stop postgres-db python-api apache-web
```

## Container entfernen

```bash
podman rm postgres-db python-api apache-web
```

## Hinweise

- Es sollte `mysecretpassword` durch ein sicheres Passwort ersetzt werden, wenn man das Projekt seriös nutzen möchte.
- Die Datenbankabfragen und HTML-Seiten können je nach Bedarf angepasst werden.

# CONTRIBUTING

## How to run the Dockerfile locally

```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE NAME sh -c "flask run"
```
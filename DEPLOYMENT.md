# Deployment Guide

## GitHub Actions CI/CD Pipeline

The workflow automatically triggers on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

### Pipeline Steps

1. **Build Job**: Tests on Python 3.9, 3.10, 3.11
   - Installs dependencies
   - Runs linting (flake8)
   - Runs tests (pytest)
   - Validates file structure

2. **Docker Build Job**: Creates Docker image
   - Builds container image
   - Caches layers for faster builds

3. **Deploy Job**: Runs only on `main` branch push
   - Creates deployment artifact
   - Uploads to GitHub Actions artifacts

## Local Development

### Using Docker Compose
```bash
docker-compose up
```
Access at `http://localhost:5000`

### Direct Python
```bash
pip install -r requirements.txt
python server.py
```

## Docker Deployment

### Build Image
```bash
docker build -t markitdown-webapp:latest .
```

### Run Container
```bash
docker run -p 5000:5000 markitdown-webapp:latest
```

## Cloud Deployment Options

### Heroku
```bash
heroku create your-app-name
git push heroku main
```

### AWS EC2
1. Download artifact from GitHub Actions
2. Extract on server
3. Install dependencies
4. Run with gunicorn: `gunicorn -w 4 -b 0.0.0.0:5000 server:app`

### Railway/Render
1. Connect GitHub repository
2. Auto-deploys on push to main

### DigitalOcean App Platform
1. Connect GitHub repository
2. Select Python as runtime
3. Set start command: `python server.py`

## Environment Variables (for production)

Create a `.env` file or set in deployment platform:
```
FLASK_ENV=production
FLASK_DEBUG=0
```

## Monitoring Deployments

Check GitHub Actions tab for:
- Build status
- Linting results
- Test results
- Deployment artifacts

# NXTG-Forge Deployment Guide

> Complete deployment instructions for all environments

## Prerequisites

### Local Development

- Python 3.9+
- Node.js 16+
- Docker & Docker Compose
- Git
- Claude Code CLI

### Production

- Container registry (Docker Hub, GCR, ECR)
- Kubernetes cluster OR VPS with Docker
- CI/CD platform (GitHub Actions recommended)
- Domain name and SSL certificates
- Database (PostgreSQL recommended)
- Cache (Redis recommended)

---

## Development Deployment

### 1. Initial Setup

```bash
# Clone repository
git clone <repository-url>
cd nxtg-forge

# Install dependencies
make dev-install

# Or manually:
pip install -r requirements.txt
pip install -e ".[dev]"
npm install
pre-commit install
```

### 2. Configuration

Create `.env` file:

```bash
# Copy example
cp .env.example .env

# Edit with your values
DATABASE_URL=postgresql://user:password@localhost:5432/forge_db
REDIS_URL=redis://localhost:6379
DEBUG=true
SECRET_KEY=your-secret-key-here
```

### 3. Start Services

```bash
# Start all services with Docker Compose
make docker-up

# Or manually:
docker-compose up -d
```

### 4. Verify Installation

```bash
# Run tests
make test

# Check status
python forge/cli.py status

# Run health check
make health
```

---

## Docker Deployment

### Build Image

```bash
# Build production image
docker build -t nxtg-forge:1.0.0 .

# Or use make
make docker-build
```

### Run Container

```bash
# Run with environment variables
docker run -d \
  --name nxtg-forge \
  -e DATABASE_URL=postgresql://... \
  -e REDIS_URL=redis://... \
  -v $(pwd)/.claude:/app/.claude \
  -p 8000:8000 \
  nxtg-forge:1.0.0
```

### Docker Compose

```bash
# Production compose
docker-compose -f docker-compose.prod.yml up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

## Kubernetes Deployment

### 1. Create Namespace

```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: nxtg-forge
```

```bash
kubectl apply -f namespace.yaml
```

### 2. Create Secrets

```bash
# Create secret for environment variables
kubectl create secret generic nxtg-forge-secrets \
  --from-literal=database-url='postgresql://...' \
  --from-literal=redis-url='redis://...' \
  --from-literal=secret-key='your-secret-key' \
  -n nxtg-forge
```

### 3. Deploy Application

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nxtg-forge
  namespace: nxtg-forge
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nxtg-forge
  template:
    metadata:
      labels:
        app: nxtg-forge
    spec:
      containers:
      - name: forge
        image: your-registry/nxtg-forge:1.0.0
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: nxtg-forge-secrets
              key: database-url
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: nxtg-forge-secrets
              key: redis-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

```bash
kubectl apply -f deployment.yaml
```

### 4. Create Service

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: nxtg-forge-service
  namespace: nxtg-forge
spec:
  type: LoadBalancer
  selector:
    app: nxtg-forge
  ports:
  - port: 80
    targetPort: 8000
    protocol: TCP
```

```bash
kubectl apply -f service.yaml
```

### 5. Create Ingress

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nxtg-forge-ingress
  namespace: nxtg-forge
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - forge.yourdomain.com
    secretName: nxtg-forge-tls
  rules:
  - host: forge.yourdomain.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nxtg-forge-service
            port:
              number: 80
```

```bash
kubectl apply -f ingress.yaml
```

---

## VPS Deployment

### Using Docker Compose

```bash
# 1. SSH into VPS
ssh user@your-vps-ip

# 2. Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# 3. Clone repository
git clone <repository-url>
cd nxtg-forge

# 4. Configure environment
cp .env.example .env
nano .env  # Edit with production values

# 5. Start services
docker-compose -f docker-compose.prod.yml up -d

# 6. Configure nginx reverse proxy
sudo apt install nginx

# 7. Create nginx config
sudo nano /etc/nginx/sites-available/nxtg-forge
```

Nginx configuration:

```nginx
server {
    listen 80;
    server_name forge.yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/nxtg-forge /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Install SSL with Certbot
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d forge.yourdomain.com
```

---

## CI/CD Deployment

### GitHub Actions

Already configured in `.github/workflows/ci.yml`.

**To enable automated deployment:**

1. Add secrets to GitHub:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`
   - `K8S_CONFIG` (base64 encoded kubeconfig)

2. Update workflow to include deployment:

```yaml
# Add to .github/workflows/ci.yml

deploy-production:
  name: Deploy to Production
  runs-on: ubuntu-latest
  needs: build
  if: github.ref == 'refs/heads/main'

  steps:
    - uses: actions/checkout@v4

    - name: Log in to Docker Hub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build and push
      uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: |
          your-registry/nxtg-forge:latest
          your-registry/nxtg-forge:${{ github.sha }}

    - name: Deploy to Kubernetes
      uses: azure/k8s-deploy@v4
      with:
        manifests: |
          k8s/deployment.yaml
          k8s/service.yaml
        images: |
          your-registry/nxtg-forge:${{ github.sha }}
        kubeconfig: ${{ secrets.K8S_CONFIG }}
```

---

## Database Setup

### PostgreSQL

```bash
# Using Docker
docker run -d \
  --name postgres \
  -e POSTGRES_USER=forge \
  -e POSTGRES_PASSWORD=secure_password \
  -e POSTGRES_DB=forge_db \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:15-alpine

# Or use managed service (recommended for production):
# - AWS RDS
# - Google Cloud SQL
# - DigitalOcean Managed Databases
# - Heroku Postgres
```

### Redis

```bash
# Using Docker
docker run -d \
  --name redis \
  -p 6379:6379 \
  -v redis_data:/data \
  redis:7-alpine

# Or use managed service:
# - AWS ElastiCache
# - Google Cloud Memorystore
# - Redis Cloud
```

---

## Monitoring & Logging

### Application Logs

```bash
# View logs
docker-compose logs -f forge

# Or in Kubernetes
kubectl logs -f deployment/nxtg-forge -n nxtg-forge

# Save logs to file
docker-compose logs forge > app.log
```

### Health Monitoring

```bash
# Health check endpoint
curl http://localhost:8000/health

# Detailed status
python forge/cli.py health --detail
```

### Metrics (Optional)

Install Prometheus + Grafana:

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'nxtg-forge'
    static_configs:
      - targets: ['nxtg-forge:8000']
```

---

## Backup & Recovery

### State Backups

```bash
# Backup state directory
tar -czf state-backup-$(date +%Y%m%d).tar.gz .claude/

# Restore state
tar -xzf state-backup-20250104.tar.gz
```

### Database Backups

```bash
# Backup PostgreSQL
docker exec postgres pg_dump -U forge forge_db > backup.sql

# Restore
docker exec -i postgres psql -U forge forge_db < backup.sql
```

### Automated Backups

```bash
# Add to crontab
crontab -e

# Daily backup at 2 AM
0 2 * * * /path/to/backup-script.sh
```

---

## Security Hardening

### 1. Environment Variables

- Never commit `.env` files
- Use secrets management (Vault, AWS Secrets Manager)
- Rotate credentials regularly

### 2. HTTPS Only

- Use Let's Encrypt for SSL
- Enforce HTTPS redirects
- Set HSTS headers

### 3. Firewall Rules

```bash
# Allow only necessary ports
ufw allow 22/tcp   # SSH
ufw allow 80/tcp   # HTTP
ufw allow 443/tcp  # HTTPS
ufw enable
```

### 4. Updates

```bash
# Keep system updated
apt update && apt upgrade -y

# Update Docker images
docker-compose pull
docker-compose up -d
```

---

## Scaling

### Horizontal Scaling (Kubernetes)

```bash
# Scale deployment
kubectl scale deployment/nxtg-forge --replicas=5 -n nxtg-forge

# Auto-scaling
kubectl autoscale deployment/nxtg-forge \
  --min=3 \
  --max=10 \
  --cpu-percent=70 \
  -n nxtg-forge
```

### Vertical Scaling

Update resource limits in deployment.yaml:

```yaml
resources:
  requests:
    memory: "512Mi"
    cpu: "500m"
  limits:
    memory: "1Gi"
    cpu: "1000m"
```

---

## Troubleshooting

### Common Issues

**Container won't start:**

```bash
# Check logs
docker logs nxtg-forge

# Check environment
docker exec nxtg-forge env
```

**Database connection fails:**

```bash
# Test connection
docker exec forge psql $DATABASE_URL -c "SELECT 1"

# Check network
docker network inspect nxtg-forge_default
```

**High memory usage:**

```bash
# Check resource usage
docker stats

# Restart services
docker-compose restart
```

---

## Rollback Procedures

### Docker

```bash
# Rollback to previous image
docker-compose down
docker-compose pull your-registry/nxtg-forge:previous-tag
docker-compose up -d
```

### Kubernetes

```bash
# Rollback deployment
kubectl rollout undo deployment/nxtg-forge -n nxtg-forge

# Check rollout history
kubectl rollout history deployment/nxtg-forge -n nxtg-forge

# Rollback to specific revision
kubectl rollout undo deployment/nxtg-forge --to-revision=2 -n nxtg-forge
```

---

## Performance Tuning

### Database

- Enable connection pooling
- Add appropriate indexes
- Regular VACUUM and ANALYZE

### Application

- Enable caching
- Use async/await patterns
- Optimize queries

### Infrastructure

- Use CDN for static assets
- Enable gzip compression
- Configure load balancer

---

*Last Updated: 2025-01-04*
*Version: 1.0.0*

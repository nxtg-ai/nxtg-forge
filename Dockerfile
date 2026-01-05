# NXTG-Forge - Production Dockerfile

FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY forge/ ./forge/
COPY .claude/ ./.claude/
COPY scripts/ ./scripts/
COPY pyproject.toml ./
COPY README.md ./

# Create necessary directories
RUN mkdir -p /app/.claude/tmp /app/.claude/checkpoints

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import forge; print('healthy')" || exit 1

# Default command
CMD ["python", "-m", "forge.cli", "status"]

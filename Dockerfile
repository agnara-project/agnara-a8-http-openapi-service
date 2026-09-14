# --- Stage 1: Build ---
FROM python:3.14-slim AS builder

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /build

# Install dependencies required for building if any
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy packaging configuration and install dependencies into a local user directory
COPY pyproject.toml README.md ./
COPY src/ src/

# Install the application and its dependencies
# Using --prefix=/install to separate built dependencies for the final stage
RUN pip install --no-cache-dir --prefix=/install .


# --- Stage 2: Production ---
FROM python:3.14-slim AS production

# Security: Create a non-root user and group
RUN groupadd -r agnara && useradd -r -g agnara -s /usr/sbin/nologin agnara

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

WORKDIR /app

# Copy the pre-built dependencies from the builder stage
COPY --from=builder /install /usr/local

# Copy application execution files
COPY --chown=agnara:agnara src/ src/
COPY --chown=agnara:agnara main.py .

# Switch to the non-root user
USER agnara

# Expose the API port
EXPOSE 8000

# Strict command avoiding shell wrapping
CMD ["python", "main.py"]

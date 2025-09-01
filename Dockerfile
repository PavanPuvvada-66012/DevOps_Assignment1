# Example minimal Dockerfile
FROM python:3.11-slim
# Install Tk dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    tcl \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "src/aceest_fitness.py"]

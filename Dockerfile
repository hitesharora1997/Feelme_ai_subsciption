# Stage 1: Build the application
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Create a smaller runtime image
FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /app/venv ./venv

COPY --from=builder /app .

ENV FLASK_APP=app/main.py
ENV PATH="/app/venv/bin:$PATH"

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

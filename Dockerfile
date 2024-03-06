FROM python:3.12-alpine AS builder
RUN apk update
WORKDIR /app
COPY app.py .

FROM python:3.12-alpine
COPY --from=builder /app .
RUN apk update
COPY requirements* ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["python3", "app.py"]``
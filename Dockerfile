FROM python:3.10-slim as base

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

FROM base as unit_test
COPY . /app
CMD ["python", "-m", "pytest", "--cov=flask_starterkit", "--cov-report=term-missing"]

FROM base as production
COPY . /app
CMD ["python", "run.py"]

FROM base as localdev

CMD ["python", "run.py"]

FROM python:3.10-slim as base

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /flask_starterkit
COPY . /flask_starterkit

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /flask_starterkit
USER appuser

FROM base as unit_test
# Run pytest with coverage report generation
CMD ["python", "-m", "pytest", "--cov=flask_starterkit", "--cov-report=term-missing"]

FROM base as prod

CMD ["flask", "run", "--host", "0.0.0.0"]


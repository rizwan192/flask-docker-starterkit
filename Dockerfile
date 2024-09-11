FROM python:3.10-slim as base

EXPOSE 5000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app
RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

FROM base as unit_test
CMD ["python", "-m", "pytest", "--cov=flask_starterkit", "--cov-report=term-missing"]

FROM base as production
CMD ["flask", "run", "--host", "0.0.0.0"]


FROM base as localdev
CMD ["python", "run.py"]

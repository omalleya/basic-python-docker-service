FROM --platform=linux/amd64 python:3.9-slim

WORKDIR ./
COPY . ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install

EXPOSE 80
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
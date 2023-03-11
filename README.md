# 🌶️ flask-docker-starterkit

A simple starterkit providing everything you need to start a new `flask` project

## 🧰 Build the image

To build the docker image, simply open a terminal and run the following command:

```bash
docker-compose build
```

## 🖥️ Run the image

To run the image in a docker container, simply open a terminal and run the following command:

```bash
docker-compose up flaskdockerstarterkit
```

The project will be available on the following URI: `http://127.0.0.1:5000`

## 🧪 Run tests

To run the tests, please run the following command in your terminal:

```bash
docker-compose up test-runner
```

## 🕵️ Environment Variables

You need to have a `.env` file containing all the keys and values required.

You can refer to the `.env.example` file

## 🗓️ Features

- Up and running `flask` server
- Containerized application
- Unit tests (in progress)

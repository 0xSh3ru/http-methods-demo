# HTTP Methods Demo

A simple demonstration application that showcases how different HTTP methods work and how to test them using `curl`.

## Prerequisites

Make sure the following tools are installed on your system:

- `git`
- `python3`

## Running the Application

Clone the repository and start the development server:

```bash
git clone git@github.com:0xSh3ru/http-methods-demo.git
cd http-methods-demo
python3 -m venv .venv
source .venv/bin/activate
python3 app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

# Testing HTTP Methods with cURL

The following examples demonstrate how to interact with each endpoint using `curl`.

**Base URL**

```text
http://127.0.0.1:5000
```

---

## GET

Retrieve all users.

```bash
curl -v http://127.0.0.1:5000/users
```

Retrieve a specific user.

```bash
curl -v http://127.0.0.1:5000/users/1
```

---

## POST

Create a new user.

```bash
curl -v \
-X POST \
-H "Content-Type: application/json" \
-d '{
    "name":"Sheru",
    "email":"sheru@test.com"
}' \
http://127.0.0.1:5000/users
```

---

## PUT

Replace an existing user.

```bash
curl -v \
-X PUT \
-H "Content-Type: application/json" \
-d '{
    "name":"Updated User",
    "email":"updated@test.com"
}' \
http://127.0.0.1:5000/users/1
```

---

## PATCH

Update one or more fields of an existing user.

```bash
curl -v \
-X PATCH \
-H "Content-Type: application/json" \
-d '{
    "email":"new@test.com"
}' \
http://127.0.0.1:5000/users/1
```

---

## DELETE

Delete a user.

```bash
curl -v \
-X DELETE \
http://127.0.0.1:5000/users/1
```

---

## HEAD

Retrieve only the response headers.

```bash
curl -I http://127.0.0.1:5000/health
```

Or explicitly specify the method:

```bash
curl -v \
-X HEAD \
http://127.0.0.1:5000/health
```

---

## OPTIONS

Retrieve the HTTP methods supported by an endpoint.

```bash
curl -v \
-X OPTIONS \
http://127.0.0.1:5000/methods
```

Expected response header:

```http
Allow: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, QUERY
```

---

## QUERY

Perform a read-only query by sending a request body.

Search by name:

```bash
curl -v \
-X QUERY \
-H "Content-Type: application/json" \
-d '{
    "name":"Sheru"
}' \
http://127.0.0.1:5000/users/search
```

Search by email:

```bash
curl -v \
-X QUERY \
-H "Content-Type: application/json" \
-d '{
    "email":"test.com"
}' \
http://127.0.0.1:5000/users/search
```

---

## TRACE

Echo the received request back to the client.

```bash
curl -v \
-X TRACE \
http://127.0.0.1:5000/trace
```

> **Note:** TRACE is commonly disabled on production servers for security reasons.

---

## CONNECT

This demo application does **not** implement the CONNECT method because CONNECT is designed to establish TCP tunnels through HTTP proxies rather than communicate directly with web applications.

Example request to an HTTP proxy:

```bash
curl -v \
-X CONNECT \
http://proxy.example.com:8080
```

---

# HTTP Method Summary

| Method | Endpoint | Purpose |
|---------|----------|---------|
| GET | `/users` | Retrieve all users |
| GET | `/users/1` | Retrieve a specific user |
| POST | `/users` | Create a new user |
| PUT | `/users/1` | Replace an existing user |
| PATCH | `/users/1` | Partially update a user |
| DELETE | `/users/1` | Delete a user |
| HEAD | `/health` | Retrieve response headers only |
| OPTIONS | `/methods` | List supported HTTP methods |
| QUERY | `/users/search` | Perform a read-only query with a request body |
| TRACE | `/trace` | Echo the received request |
| CONNECT | Proxy server | Establish an HTTP tunnel through a proxy |

---

# Common cURL Options

| Option | Description |
|--------|-------------|
| `-v` | Display verbose request and response information |
| `-i` | Include response headers in the output |
| `-I` | Send a HEAD request |
| `-X <METHOD>` | Specify the HTTP method |
| `-H` | Add an HTTP request header |
| `-d` | Send a request body |
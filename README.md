# Flask TODO API

A RESTful API for managing tasks — built with Flask, structured with Blueprints, and designed with clean separation of concerns.

---

## Project Structure

```
flask-module/
├── app.py              # Entry point — registers all Blueprints
├── routes.py           # All task endpoints (Blueprint)
├── models.py           # In-memory data layer + CRUD logic
├── errors.py           # Global error handlers (Blueprint)
├── todo_app.py         # Legacy monolith — Part 1 & 2 history
├── requirements.txt
├── classwork/          # In-class exercises and practice files
│   ├── app_testing.py
│   ├── error_handling_exercise1.py
│   └── hands_on_labs.py
├── postman/            # Exported Postman collections
│   ├── todo-api.postman_collection.json
│   ├── jsonplaceholder-api.postman_collection.json
│   └── pokeapi.postman_collection.json
└── screenshots/
    ├── postman-results/    # Test run results from various collections
    └── performance/        # TODO API performance test results
```

### Separation of Concerns

| File | Responsibility |
|---|---|
| `app.py` | App factory — wires Blueprints together, nothing else |
| `routes.py` | HTTP layer — receives requests, raises exceptions, returns responses |
| `models.py` | Data layer — all task logic and in-memory storage |
| `errors.py` | Error layer — catches all exceptions, formats unified JSON |

---

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/Dude775/flask-module.git
cd flask-module

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python app.py
```

Server runs at: `http://127.0.0.1:5000`

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/tasks` | Get all tasks |
| `GET` | `/tasks/<task_id>` | Get task by ID |
| `POST` | `/tasks` | Create a new task |
| `PUT` | `/tasks/<task_id>` | Update a task |
| `DELETE` | `/tasks/<task_id>` | Delete a task |

---

## Request & Response Examples

### GET /tasks
```json
[
  { "id": "1", "title": "Learn Flask", "completed": false },
  { "id": "2", "title": "Build API", "completed": false },
  { "id": "3", "title": "Test with Postman", "completed": true }
]
```

### POST /tasks
**Request:**
```json
{ "title": "New Task" }
```
**Response `201`:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "New Task",
  "completed": false
}
```

### PUT /tasks/:id
**Request:**
```json
{ "completed": true }
```

### DELETE /tasks/:id
**Response `200`:**
```json
{ "message": "deleted successfuly" }
```

---

## Error Handling

All errors return a **unified JSON format**:

```json
{
  "error": "error name",
  "message": "description of what went wrong",
  "status": 404
}
```

| Code | Trigger |
|---|---|
| `400` | Missing or empty `title` field |
| `404` | Task ID not found |
| `405` | Wrong HTTP method for endpoint |
| `422` | Unprocessable entity |
| `500` | Unexpected server error |

---

## Postman Tests

All 4 required test cases pass:

| # | Request | Expected | Result |
|---|---|---|---|
| 1 | `GET /tasks` | `200` | ✅ Pass |
| 2 | `GET /tasks/999` | `404` | ✅ Pass |
| 3 | `POST /tasks` (no body) | `400` | ✅ Pass |
| 4 | `POST /tasks/1` | `405` | ✅ Pass |

Postman Collection: `postman/todo-api.postman_collection.json`

---

## Performance

Tested with Postman Performance Runner — 20 virtual users, 10 minutes:

| Metric | Result |
|---|---|
| Total requests | ~33,000 |
| Requests/second | ~500 req/s |
| Avg response time | 7 ms |
| P99 | 29 ms |
| Failure % | 0.00% |

> Performance screenshots available in `screenshots/performance/`

---

## Evolution

| Part | What changed |
|---|---|
| Part 1 | Basic CRUD in single file (`todo_app.py`), int IDs with counter |
| Part 2 | Migrated to UUID — unique, JSON-safe, collision-free IDs |
| Part 3 | Blueprints, global error handlers, unified JSON error format |

---

## Tech Stack

- **Python 3**
- **Flask** — web framework
- **Werkzeug** — HTTP exceptions (`NotFound`, `BadRequest`, `HTTPException`)
- **uuid** — unique task ID generation
- **Postman** — API testing & performance testing

---

## Notes

- Data is stored **in-memory only** — restarting the server resets all tasks to the 3 hardcoded defaults.
- This project is intentionally kept simple — no database, no authentication, no deployment config.
- `todo_app.py` is preserved as historical reference for Parts 1 and 2.
- `classwork/` contains in-class exercises not directly related to the TODO API project.
- `postman/` contains exported collections from various API practice sessions during the course.

# Candidate Assessment: Spec-Driven Development With Codegen Tools

This assessment evaluates how you use modern code generation tools (for example `5.2-Codex`, `Claude`, `Copilot`, and similar) to design, build, and test a software application using a spec-driven development pattern. You may build a frontend, a backend, or both.

## Goals
- Build a working application with at least one meaningful feature.
- Create a testing framework to validate the application.
- Demonstrate effective use of code generation tools to accelerate delivery.
- Show clear, maintainable engineering practices.

## Deliverables
- Application source code in this repository.
- A test suite and test harness that can be run locally.
- Documentation that explains how to run the app and the tests.

## Scope Options
Pick one:
- Frontend-only application.
- Backend-only application.
- Full-stack application.

Your solution should include at least one real workflow, for example:
- Create and view a resource.
- Search or filter data.
- Persist data in memory or storage.

## Rules
- You must use a code generation tool (for example `5.2-Codex`, `Claude`, or similar). You can use multiple tools.
- You must build the application and a testing framework for it.
- The application and tests must run locally.
- Do not include secrets or credentials in this repository.

## Evaluation Criteria
- Working product: Does the app do what it claims?
- Test coverage: Do tests cover key workflows and edge cases?
- Engineering quality: Clarity, structure, and maintainability.
- Use of codegen: How effectively you used tools to accelerate work.
- Documentation: Clear setup and run instructions.

## What to Submit
- When you are complete, put up a Pull Request against this repository with your changes.
- A short summary of your approach and tools used in your PR submission
- Any additional information or approach that helped you.

++++++++++++++++++++++++++++++++++++++++++++++

## Local Setup and Usage

### Clone the Repository
```bash
https://github.com/jeevan-puli/spec-driven-development/tree/resource-management-api
```
check out the feature branch:
```bash
git checkout resource-management-api
```

### Create and Activate Virtual Environment (Python)
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Run the Application
Start the FastAPI server locally:
```bash
uvicorn app.main:app --reload
```
Verify the API is running by opening:
```bash
http://127.0.0.1:8000/docs
```

### You can also manually verify the API:
```bash
curl -X POST http://127.0.0.1:8000/resources \
  -H "Content-Type: application/json" \
  -d '{"name":"example","type":"demo"}'
```
### Run Tests (without readable logs)
Execute the full test suite:
```bash
pytest
```
### Run Tests (with readable logs)
Execute the full test suite:
```bash
pytest --log-cli-level=INFO
```

## Code Generation Usage
Modern code generation tools (ChatGPT / Codex-style models) were used to
accelerate scaffolding of the API and test cases. All generated code was
reviewed and refined manually to ensure correctness, determinism, and
coverage of edge cases.

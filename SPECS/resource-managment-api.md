# Feature Spec: Resource Management API

## Goal
Provide a simple backend API to create, retrieve, and filter resources in a spec-driven manner,
serving as a test target for API and contract testing.

## Scope
### In:
- Create a resource via API
- Retrieve all resources
- Filter resources by type
- Validate request and response schemas

### Out:
- Authentication / authorization
- External persistence (DB, cloud services)
- Frontend UI

## Requirements
- The API must support creating a resource with required fields.
- Each resource must be assigned a unique ID.
- Resources must be retrievable via a GET endpoint.
- Filtering by resource type must be supported.
- Invalid requests must return clear error responses.
- API responses must conform to a stable schema.

## Acceptance Criteria
- [ ] POST /resources creates a resource with valid input
- [ ] GET /resources returns all created resources
- [ ] GET /resources?type=<type> filters resources correctly
- [ ] Missing required fields return a 400 error
- [ ] Invalid resource type returns a validation error
- [ ] Response schema remains consistent across requests

<!-- SYNC IMPACT REPORT:
Version change: 1.0.0 → 1.0.0
Modified principles: None (new constitution)
Added sections: All sections
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ Updated
  - .specify/templates/spec-template.md: ✅ Updated
  - .specify/templates/tasks-template.md: ✅ Updated
  - .specify/templates/commands/*.md: ⚠ Pending review
  - README.md: ⚠ Pending review
Follow-up TODOs: None
-->

# Hackathon Todo Project Constitution

## Core Principles

### 1. Spec-Driven Development (MANDATORY)
No feature may be implemented without a written specification. Claude Code must read and reference specs before implementation. Specs are the single source of truth. If requirements change, specs must be updated first, not code.

### 2. Agentic Dev Stack Workflow (MANDATORY)
Every feature must follow this workflow: 1) Write or update specification, 2) Generate implementation plan, 3) Break plan into tasks, 4) Implement tasks using Claude Code, 5) Review output and iterate via spec updates. Manual coding by the user is not allowed - all code must be generated or modified by Claude Code.

### 3. Phase-Based Evolution
The project evolves through five strictly ordered phases: Phase I (In-Memory Python Console App), Phase II (Full-Stack Web Application), Phase III (AI-Powered Todo Chatbot), Phase IV (Local Kubernetes Deployment), and Phase V (Advanced Cloud Deployment). Each phase builds on the previous phase, expands specs, never deletes them, and must remain runnable and reviewable independently.

### 4. Phase I: Console Todo App Foundation
Build a command-line Todo application using Python that stores all data in memory only. Constraints: No databases, no file storage, no external APIs, no persistence across restarts. Required features: Add Task, Delete Task, Update Task, View Task List, Mark Task as Complete. Technical rules: Python version 3.13+, in-memory storage only, clean architecture and separation of concerns, clear CLI feedback for all operations.

### 5. Phase II: Full-Stack Web Application
Transform the Phase I console app into a multi-user, authenticated web application with persistent storage. Required capabilities: All Phase I features must exist in web form, RESTful API implementation, responsive frontend UI, user authentication and isolation, persistent database storage. Technology stack: Next.js 16+ (App Router), FastAPI (Python), SQLModel, Neon Serverless PostgreSQL, Better Auth.

### 6. Authentication and Security Guarantees
Better Auth runs only on frontend, backend authentication is enforced via JWT. JWT tokens must be issued by Better Auth, attached to every API request, verified by FastAPI middleware. Backend must not trust frontend blindly. Each user can only access their own tasks. All API endpoints require valid JWT. Unauthorized requests return 401 Unauthorized. User ID from JWT must match route parameters.

## REST API Constitutional Rules

### Endpoint Rules
All routes must live under `/api/`. All requests require `Authorization: Bearer <token>`. Task ownership enforced on every operation.

### Canonical Endpoints
- `GET /api/{user_id}/tasks`
- `POST /api/{user_id}/tasks`
- `GET /api/{user_id}/tasks/{id}`
- `PUT /api/{user_id}/tasks/{id}`
- `DELETE /api/{user_id}/tasks/{id}`
- `PATCH /api/{user_id}/tasks/{id}/complete`

## Monorepo Constitution

### Repository Structure (MANDATORY)
```
hackathon-todo/
├── .spec-kit/
├── specs/
│   ├── overview.md
│   ├── sp.constitution.md
│   ├── architecture.md
│   ├── features/
│   ├── api/
│   ├── database/
│   └── ui/
├── CLAUDE.md
├── frontend/
│   └── CLAUDE.md
├── backend/
│   └── CLAUDE.md
├── docker-compose.yml
└── README.md
```

### Reason
Single Claude context, cross-stack changes are easier, specs remain centralized and authoritative.

## CLAUDE.md Hierarchy Rule

Claude Code must respect instruction priority:
1. `specs/sp.constitution.md` (Highest authority)
2. Root `CLAUDE.md`
3. Feature / API / DB specs
4. Folder-level `CLAUDE.md`
5. File-level context

If conflict exists → higher authority wins

## Phase III: AI-Powered Todo Chatbot

Introduce an AI chatbot interface that understands natural language task commands, interacts with existing task system, and respects authentication and user boundaries. Chatbot must not bypass REST API, uses MCP-style tools or defined API calls, and all chatbot behavior must be spec-defined.

## Phase IV: Local Kubernetes Deployment

Deploy the system locally using Kubernetes with containerized frontend and backend, local cluster (Docker Desktop / Rancher Desktop), environment-based configuration, and secure secrets handling.

## Phase V: Advanced Cloud Deployment

Deploy production-ready cloud infrastructure with scalability, environment separation, secure secrets, and observability readiness.

## Final Constitutional Rules (NON-NEGOTIABLE)

- ❌ No coding without specs
- ❌ No skipping phases
- ❌ No breaking previous functionality
- ✅ Specs evolve, code follows
- ✅ Claude Code is the primary developer
- ✅ Reviewability is as important as functionality

## Governance

This document overrides: README, Comments, Prompts, Developer assumptions.

If it's not allowed here, it's not allowed anywhere.

**Version**: 1.0.0 | **Ratified**: 2026-01-17 | **Last Amended**: 2026-01-17
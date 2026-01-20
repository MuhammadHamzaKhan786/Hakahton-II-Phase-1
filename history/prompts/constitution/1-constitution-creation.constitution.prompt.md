---
id: 1
title: constitution-creation
stage: constitution
date: 2026-01-17
surface: agent
model: claude-haiku-4-5-20251001
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution, setup, hackathon-todo]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
/sp.constitution

# SP Constitution – Hackathon Todo Project



\\## Purpose

This document defines the \\*\\*constitutional rules, development philosophy, and non-negotiable constraints\\*\\* for the Hackathon Todo project.

All development across all phases \\*\\*must strictly follow this constitution\\*\\*.





\\## Core Principles



\\### 1. Spec-Driven Development (MANDATORY)

\\- No feature may be implemented without a written specification.

\\- Claude Code \\*\\*must read and reference specs\\*\\* before implementation.

\\- Specs are the \\*\\*single source of truth\\*\\*.

\\- If requirements change, \\*\\*specs must be updated first\\*\\*, not code.



\\-\\-\\-



\\### 2. Agentic Dev Stack Workflow (MANDATORY)

Every feature must follow this workflow:



1\\. Write or update specification

2\\. Generate implementation plan

3\\. Break plan into tasks

4\\. Implement tasks using Claude Code

5\\. Review output and iterate via spec updates



❌ Manual coding by the user is \\*\\*not allowed\\*\\*

✅ All code must be generated or modified by Claude Code



\\-\\-\\-



\\### 3. Phase-Based Evolution

The project evolves through \\*\\*five strictly ordered phases\\*\\*.



| Phase | Description |

|-----|------------|

| Phase I | In-Memory Python Console App |

| Phase II | Full-Stack Web Application |

| Phase III | AI-Powered Todo Chatbot |

| Phase IV | Local Kubernetes Deployment |

| Phase V | Advanced Cloud Deployment |



Each phase:

\\- Builds on the previous phase

\\- Expands specs, never deletes them

\\- Must remain runnable and reviewable independently



\\-\\-\\-



\\## Phase I: Console Todo App (FOUNDATIONAL PHASE)



\\### Objective

Build a \\*\\*command-line Todo application\\*\\* using Python that stores all data \\*\\*in memory only\\*\\*.



\\### Constraints

\\- No databases

\\- No file storage

\\- No external APIs

\\- No persistence across restarts



\\### Required Features (ALL MANDATORY)

1\\. Add Task

2\\. Delete Task

3\\. Update Task

4\\. View Task List

5\\. Mark Task as Complete



\\### Technical Rules

\\- Python version: \\*\\*3.13+\\*\\*

\\- In-memory storage only (lists, dicts, objects)

\\- Clean architecture and separation of concerns

\\- Clear CLI feedback for all operations



\\### Quality Standards

\\- Single Responsibility Principle

\\- Predictable function behavior

\\- Explicit error handling (invalid IDs, empty input)

\\- Readable, maintainable structure



\\-\\-\\-



\\## Phase II: Full-Stack Web Application



\\### Objective

Transform the Phase I console app into a \\*\\*multi-user, authenticated web application\\*\\* with persistent storage.



\\### Required Capabilities

\\- All Phase I features must exist in web form

\\- RESTful API implementation

\\- Responsive frontend UI

\\- User authentication and isolation

\\- Persistent database storage



\\### Technology Stack

| Layer | Technology |

|----|----|

| Frontend | Next.js 16+ (App Router) |

| Backend | FastAPI (Python) |

| ORM | SQLModel |

| Database | Neon Serverless PostgreSQL |

| Authentication | Better Auth |

| Spec System | Claude Code + Spec-Kit Plus |



\\-\\-\\-



\\### Authentication Constitution (NON-NEGOTIABLE)



\\- Better Auth runs \\*\\*only on frontend\\*\\*

\\- Backend authentication is enforced via \\*\\*JWT\\*\\*

\\- JWT tokens must be:

 &nbsp; - Issued by Better Auth

 &nbsp; - Attached to every API request

 &nbsp; - Verified by FastAPI middleware

\\- Backend \\*\\*must not trust frontend blindly\\*\\*

\\- Each user can only access their own tasks

\\- All API endpoints require valid JWT

\\- Unauthorized requests return `401 Unauthorized`

\\- User ID from JWT must match route parameters



\\-\\-\\-



\\## REST API Constitutional Rules



\\### Endpoint Rules

\\- All routes must live under `/api/`

\\- All requests require `Authorization: Bearer <token>`

\\- Task ownership enforced on \\*\\*every operation\\*\\*



\\### Canonical Endpoints

\\- `GET /api/{user_id}/tasks`

\\- `POST /api/{user_id}/tasks`

\\- `GET /api/{user_id}/tasks/{id}`

\\- `PUT /api/{user_id}/tasks/{id}`

\\- `DELETE /api/{user_id}/tasks/{id}`

\\- `PATCH /api/{user_id}/tasks/{id}/complete`



\\-\\-\\-



\\## Monorepo Constitution



\\### Repository Structure (MANDATORY)


hackathon-todo/

├── .spec-kit/

├── specs/

│ ├── overview.md

│ ├── sp.constitution.md

│ ├── architecture.md

│ ├── features/

│ ├── api/

│ ├── database/

│ └── ui/

├── CLAUDE.md

├── frontend/

│ └── CLAUDE.md

├── backend/

│ └── CLAUDE.md

├── docker-compose.yml

└── README.md



\\### Reason

\\- Single Claude context

\\- Cross-stack changes are easier

\\- Specs remain centralized and authoritative



\\-\\-\\-



\\## CLAUDE.md Hierarchy Rule



Claude Code must respect instruction priority:



1\\. `specs/sp.constitution.md` (Highest authority)

2\\. Root `CLAUDE.md`

3\\. Feature / API / DB specs

4\\. Folder-level `CLAUDE.md`

5\\. File-level context



If conflict exists → \\*\\*higher authority wins\\*\\*



\\-\\-\\-



\\## Phase III: AI-Powered Todo Chatbot



\\### Objective

Introduce an AI chatbot interface that:

\\- Understands natural language task commands

\\- Interacts with existing task system

\\- Respects authentication and user boundaries



\\### Rules

\\- Chatbot must not bypass REST API

\\- Uses MCP-style tools or defined API calls

\\- All chatbot behavior must be spec-defined



\\-\\-\\-



\\## Phase IV: Local Kubernetes Deployment



\\### Objective

Deploy the system locally using Kubernetes.



\\### Requirements

\\- Containerized frontend and backend

\\- Local cluster (Docker Desktop / Rancher Desktop)

\\- Environment-based configuration

\\- Secure secrets handling



\\-\\-\\-



\\## Phase V: Advanced Cloud Deployment



\\### Objective

Deploy production-ready cloud infrastructure.



\\### Expectations

\\- Scalability

\\- Environment separation

\\- Secure secrets

\\- Observability readiness



\\-\\-\\-



\\## Final Constitutional Rules (NON-NEGOTIABLE)



\\- ❌ No coding without specs

\\- ❌ No skipping phases

\\- ❌ No breaking previous functionality

\\- ✅ Specs evolve, code follows

\\- ✅ Claude Code is the primary developer

\\- ✅ Reviewability is as important as functionality



\\-\\-\\-



\\## Constitutional Authority

This document overrides:

\\- README

\\- Comments

\\- Prompts

\\- Developer assumptions



\\*\\*If it's not allowed here, it's not allowed anywhere.\\*\\*
```

## Response snapshot

I've created the constitution file for your Hackathon Todo Project based on the detailed requirements you provided. The constitution document contains all the core principles, phase-based evolution guidelines, technical requirements, and governance rules for the project. It establishes the foundation for how the project will develop through its five phases, from the initial console app to advanced cloud deployment.

## Outcome

- ✅ Impact: Created project constitution file with all required principles and governance rules
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: Continue with spec creation for Phase I
- 🧠 Reflection: Constitution provides clear framework for project evolution across all phases

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): not applicable
- Prompt variant (if applicable): not applicable
- Next experiment (smallest change to try): begin Phase I spec development
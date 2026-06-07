# Stakeholders and Ownership

| Stakeholder | Responsibility |
|---|---|
| Business Owner | Funds and approves business value |
| Product Owner | Owns scope, acceptance criteria, and release decision |
| Data Engineering | Owns raw knowledge source availability and refresh process |
| AI Engineering | Owns chunking, embeddings, retrieval, prompts, and evaluation implementation |
| Domain Experts | Validate truth and golden answers |
| QA Engineer | Owns regression testing and release checks |
| Security/Governance Owner | Owns risk review, access control, audit, and policy alignment |
| MLOps/Platform Engineer | Owns containerization, deployment, secrets, monitoring, and rollback |

## RACI-Style Ownership

| Workstream | Responsible | Accountable | Consulted |
|---|---|---|---|
| Knowledge base | Data Engineering | Business Owner | Domain Experts |
| Golden dataset | Domain Experts | Product Owner | AI Engineering, QA |
| Ingestion | AI Engineering | Data Engineering | MLOps |
| Retrieval | AI Engineering | Product Owner | Domain Experts |
| Evaluation | QA, AI Engineering | Product Owner | Domain Experts |
| Deployment | MLOps | Product Owner | Security |
| Monitoring | MLOps, AI Engineering | Security/Governance | Product Owner |

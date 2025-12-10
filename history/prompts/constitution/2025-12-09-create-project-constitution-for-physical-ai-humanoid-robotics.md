---
id: phr-001
title: Create Project Constitution for Physical AI & Humanoid Robotics
stage: constitution
date: 2025-12-09
surface: cli
model: "[UNKNOWN]"
feature: ""
branch: ""
user: "[UNKNOWN]"
command: /sp.constitution
labels: [constitution, documentation]
links:
  spec: ""
  ticket: ""
  adr: ""
  pr: ""
files:
  - .specify/memory/constitution.md
tests:
  []
---

## Prompt

/sp.constitution Project:AI/Spec-driven Docusaurus book + integrated RAG chatbot on Physical AI & Humanoid Robotics.Core Principles:- Technical accuracy based on official docs (ROS 2, Gazebo, Unity, Isaac, OpenAI).- Clear, implementation-focused explanations for CS/AI students.- Consistent, reproducible instructions across all modules and codebases.- Safety-aligned robotics and AI guidance.Key Standards:- All claims verifiable via authoritative sources.- Consistent citation style.- Runnable, clean code for ROS 2 (rclpy), Python/FastAPI, and ChatKit/Agents.- RAG chatbot answers strictly from book content.Constraints:- Docusaurus book deployed to GitHub Pages.- Tools: Spec-Kit Plus, Claude Code.- Backend: FastAPI + Neon Postgres + Qdrant Cloud + OpenAI Agents/ChatKit.- Must cover four modules: ROS 2, Gazebo/Unity, NVIDIA Isaac, VLA.- Include capstone: natural-language-guided humanoid robot task.Success Criteria:- Book fully deploys and all code works.- RAG chatbot responds accurately to book content and selected text.- Robotics pipeline descriptions are correct and reproducible.- Final output passes accuracy, clarity, and safety review.

## Response snapshot

I have created the project constitution at `.specify/memory/constitution.md` with version 1.0.0. I have also included a sync impact report within the file. I have checked the consistency of the constitution with other templates and found that `plan-template.md` needs to be updated.

## Outcome

- ✅ Impact: Created the first version of the project constitution.
- 🧪 Tests: N/A
- 📁 Files: `.specify/memory/constitution.md` created.
- 🔁 Next prompts: Follow-up to update templates.
- 🧠 Reflection: The process was smooth. The user provided clear requirements. The next step is to ensure the other templates are updated to reflect the new constitution.

## Evaluation notes (flywheel)

- Failure modes observed: ""
- Graders run and results (PASS/FAIL): ""
- Prompt variant (if applicable): ""
- Next experiment (smallest change to try): ""

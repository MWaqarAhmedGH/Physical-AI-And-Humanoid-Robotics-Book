<!--
---
sync_impact_report:
  version_change: "none → 1.0.0"
  modified_principles:
    - "New: Technical Accuracy"
    - "New: Clarity and Focus"
    - "New: Consistency and Reproducibility"
    - "New: Safety Alignment"
  added_sections:
    - "Key Standards and Constraints"
    - "Success Criteria"
  removed_sections: []
  template_updates:
    - path: ".specify/templates/plan-template.md"
      status: "pending"
    - path: ".specify/templates/spec-template.md"
      status: "pending"
    - path: ".specify/templates/tasks-template.md"
      status: "pending"
  todos: []
---
-->
# AI/Spec-driven Docusaurus book + integrated RAG chatbot on Physical AI & Humanoid Robotics Constitution

## Core Principles

### Technical Accuracy
Technical accuracy based on official docs (ROS 2, Gazebo, Unity, Isaac, OpenAI). All claims verifiable via authoritative sources. Consistent citation style.

### Clarity and Focus
Clear, implementation-focused explanations for CS/AI students.

### Consistency and Reproducibility
Consistent, reproducible instructions across all modules and codebases. Runnable, clean code for ROS 2 (rclpy), Python/FastAPI, and ChatKit/Agents.

### Safety Alignment
Safety-aligned robotics and AI guidance.

## Key Standards and Constraints

- Docusaurus book deployed to GitHub Pages.
- Tools: Spec-Kit Plus, Claude Code.
- Backend: FastAPI + Neon Postgres + Qdrant Cloud + OpenAI Agents/ChatKit.
- Must cover four modules: ROS 2, Gazebo/Unity, NVIDIA Isaac, VLA.
- Include capstone: natural-language-guided humanoid robot task.

## Success Criteria

- Book fully deploys and all code works.
- RAG chatbot responds accurately to book content and selected text.
- Robotics pipeline descriptions are correct and reproducible.
- Final output passes accuracy, clarity, and safety review.

## Governance

This Constitution is the single source of truth for project standards. All development activities, including specification, planning, and implementation, must adhere to these principles. Amendments require team consensus and will be recorded with a version bump.

**Version**: 1.0.0 | **Ratified**: 2025-12-09 | **Last Amended**: 2025-12-09
# Tasks: Module 1 — The Robotic Nervous System (ROS 2)

**Input**: Design documents from `specs/001-ros2-nervous-system/`
**Prerequisites**: plan.md, spec.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

## Path Conventions

- Paths shown below assume documentation project structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize Docusaurus project in the `docs/` directory.
- [ ] T002 Configure Docusaurus sidebars and navigation for the book in `docs/docusaurus.config.js`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [ ] T003 Create the main directory structure for the four modules in the book inside the `docs/` directory.
- [ ] T004 Create a template for chapters to ensure consistency.

---

## Phase 3: User Story 1 - Understand ROS 2 Fundamentals (Priority: P1) 🎯 MVP

**Goal**: Readers can understand the core concepts of ROS 2.

**Independent Test**: The reader can explain the roles of nodes, topics, services, and actions, and can use the command line to inspect them.

### Implementation for User Story 1

- [ ] T005 [P] [US1] Write Chapter 1: Introduction to the Robotic Nervous System in `docs/ros2-nervous-system/01-introduction.md`.
- [ ] T006 [P] [US1] Write Chapter 2: ROS 2 Nodes and Execution Model in `docs/ros2-nervous-system/02-nodes-and-execution.md`.
- [ ] T007 [P] [US1] Write Chapter 3: Topics, Publishers, and Subscribers in `docs/ros2-nervous-system/03-topics-publishers-subscribers.md`.
- [ ] T008 [US1] Create runnable examples for publishers and subscribers in a `examples/` directory.

---

## Phase 4: User Story 2 - Develop with Python and ROS 2 (Priority: P2)

**Goal**: Readers can integrate Python agents with ROS 2.

**Independent Test**: The reader can write a simple Python script using `rclpy` that subscribes to a topic, processes the data, and publishes a new message.

### Implementation for User Story 2

- [ ] T009 [P] [US2] Write Chapter 4: Services, Actions, and Inter-node Coordination in `docs/ros2-nervous-system/04-services-actions.md`.
- [ ] T010 [P] [US2] Write Chapter 5: Bridging Python Agents to ROS Control Loops with rclpy in `docs/ros2-nervous-system/05-python-agents-rclpy.md`.
- [ ] T011 [US2] Create runnable examples for services, actions, and `rclpy` integration in the `examples/` directory.

---

## Phase 5: User Story 3 - Model a Humanoid Robot (Priority: P3)

**Goal**: Readers can model a humanoid robot using URDF.

**Independent Test**: The reader can open a URDF file, identify the links and joints, and describe the relationship between them.

### Implementation for User Story 3

- [ ] T012 [P] [US3] Write Chapter 6: Understanding URDF for Humanoid Robots in `docs/ros2-nervous-system/06-urdf-for-humanoids.md`.
- [ ] T013 [US3] Create a sample URDF file for a simple humanoid robot in the `examples/` directory.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T014 Write Chapter 7: Chapter Review + Hands-on Exercises in `docs/ros2-nervous-system/07-review-and-exercises.md`.
- [ ] T015 Review all chapters for clarity, consistency, and technical accuracy.
- [ ] T016 Test all code examples in a clean ROS 2 Humble environment.
- [ ] T017 Configure and deploy the Docusaurus book to GitHub Pages.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** and **Foundational (Phase 2)** must be completed before any user story work begins.
- User stories can be implemented in parallel after Phase 2 is complete.
- **Polish (Phase 6)** depends on all user stories being complete.

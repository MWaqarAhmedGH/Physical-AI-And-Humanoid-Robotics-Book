# Quickstart: Contributing to the Docusaurus Book

This guide provides a quick overview of how to contribute to the Docusaurus book on Physical AI & Humanoid Robotics.

## Prerequisites

- Node.js and npm/yarn installed
- A GitHub account
- Familiarity with Markdown

## Getting Started

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Install dependencies**:
    ```bash
    npm install
    ```

3.  **Start the development server**:
    ```bash
    npm start
    ```
    This will open the Docusaurus site in your browser at `http://localhost:3000`.

## Content Creation Workflow

1.  **Create a feature branch**: Follow the branching model defined in `research.md`.
2.  **Generate a specification**: Use `/sp.specify` to create a new specification for the content you want to add.
3.  **Create a plan**: Use `/sp.plan` to create an implementation plan.
4.  **Write the content**: Create or edit the Markdown files in the `docs` directory.
5.  **Review and submit**: Once you are happy with your changes, create a pull request.

## Style Guide

- Follow the asset standards and content consistency guidelines defined in `research.md`.
- Ensure all code examples are runnable and tested.
- All claims must be verifiable and cited where appropriate.

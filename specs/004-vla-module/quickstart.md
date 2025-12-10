# Quickstart: Contributing to the VLA Module

This guide provides a quick overview of how to contribute to the "Vision-Language-Action (VLA)" module.

## Prerequisites

-   A working installation of ROS 2 Humble.
-   Access to OpenAI API for Whisper.
-   Familiarity with Python and LLMs is recommended.

## Getting Started

1.  **Set up your development environment**: Ensure that you have a clean ROS 2 workspace and that your OpenAI API keys are configured.
2.  **Explore the existing examples**: Before making changes, familiarize yourself with the existing voice command and LLM integration examples.
3.  **Follow the plan**: Refer to the `plan.md` and `tasks.md` files for this feature to understand the scope and a to-do list of items.

## Content Creation Workflow

1.  **Create a feature branch**: Follow the branching model defined in `research.md`.
2.  **Write the content**: Create or edit the Markdown files in the `docs/vla-module` directory.
3.  **Create or modify examples**: If you are adding new examples, create the necessary ROS 2 packages, Python scripts, or LLM prompts.
4.  **Test your changes**: Run all examples and ensure they work as expected.
5.  **Review and submit**: Once you are happy with your changes, create a pull request.

## Style Guide

-   Follow the asset standards and content consistency guidelines defined in `research.md`.
-   Ensure all code examples are runnable and tested.
-   All claims must be verifiable and cited where appropriate.
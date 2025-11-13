# UV Python Template | uv-template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a template for Python projects using [UV](https://uv.dev/) for dependency management and development workflows. It includes best practices for code quality, testing, CI/CD, security scanning, and packaging.

**Table of Contents**

## Template Overview

This template is developed using [copier](https://copier.readthedocs.io/) and is maintained by @ac-willeke. It provides a Python project structure for package development and additional setup can be added for Docker, Jupyter Notebooks, and documentation generation.

## Getting Started

### Prerequisites
<!-- Software versions, system requirements, dependencies, account requirements (APIs, services) -->

- [uv](https://docs.astral.sh/uv/getting-started/installation/)  - Python development tool
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and GitHub

Prerequisites for additional setup options:

- [Docker](https://docs.docker.com/engine/install/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)
extension

### Create a new Python project

```bash
uvx --with copier_template_extensions copier copy --trust https://github.com/ac-willeke/uv-template my-new-project
```

# UV Python Template | uv-template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a [Copier](https://copier.readthedocs.io/) template for Python projects using [UV](https://uv.dev/). It includes best practices for code quality, testing, CI/CD, security scanning, and packaging.

The base template sets up a Python package structure with UV for dependency management, pre-commit hooks, GitHub Actions for CI/CD, and PyPI publishing. Optional features can be included for Docker support, Jupyter Notebooks, and documentation generation.

A demo project created with this template is available at [ac-willeke/uv-demo](https://github.com/ac-willeke/uv-demo).

## Key Features

**Core Features:**

- UV for dependency management
- Pre-commit hooks with Ruff, MyPy
- GitHub Actions CI/CD
- PyPI publishing with trusted publishing
- Security scanning (CodeQL, Safety, Zizmor)
- Test coverage with pytest

**Optional Features:**

- Docker configuration
- Jupyter notebook support
- Documentation structure

## Getting Started

### Prerequisites
<!-- Software versions, system requirements, dependencies, account requirements (APIs, services) -->

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and GitHub

Prerequisites for additional setup options:

- [Docker](https://docs.docker.com/engine/install/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)

### Create a new Python project

1. Install `copier` with uv and generate a new project:

    ```bash
    # Install copier with uv and generate a new project
    uvx --with copier_template_extensions copier copy --trust https://github.com/ac-willeke/uv-template my-new-project
    ```

2. Follow the interactive prompts to customize your project.

    The template will ask you for:

    - Project name and description
    - Package and module names
    - Author information
    - Python version
    - Optional features (Docker, notebooks, docs)

3. Set up your development environment:

    ```bash
    cd my-new-project
    uv sync --group dev
    ```

4. Update your project from the template when needed:

    ```bash
    cd your-project
    copier update
    ```

## Acknowledgements

This project incorporates best practices from the Python and DevOps communities, including:

- Astral-sh's [uv Documentation](https://docs.astral.sh/uv/) and Docker configuration example [astral-sh/uv-docker-example](https://github.com/astral-sh/uv-docker-example)
- Eric Riddoch's [Taking Python to Production](https://www.udemy.com/course/setting-up-the-linux-terminal-for-software-development/) course
- Marvelous MLOps [MLOps with Databricks](https://www.youtube.com/results?search_query=marvelous+mlops) course

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

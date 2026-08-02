# multi-agent-ai-systems

A collection of examples, templates, and guides for building multi-agent AI systems using tools like crewAI, LangGraph, Autogen and related frameworks. The repository contains notebooks, example projects, and utilities organized by topic.

Language composition: Jupyter Notebooks (main), Python code.

## Repository structure

- 1_foundations/ — foundational examples, theory and notebooks
- 2_openai/ — OpenAI examples and integrations
- 3_crew/ — crewAI example crews (coder, debate, ...)
  - 3_crew/coder/ — Coder crew example (agents for coding tasks)
  - 3_crew/debate/ — Debate crew example (agents debating a topic)
- 4_langgraph/ — LangGraph examples and utilities
- 5_autogen/ — Autogen-based agent examples
- 6_mcp/ — MCP experiments and demos
- guides/ — longer-form guides and walkthroughs
- setup/ — platform-specific setup instructions (Windows, Mac, Linux)

## Quick start

1. Review the platform-specific setup instructions in the `setup/` folder:
   - Windows: `setup/SETUP-PC.md`
   - macOS: `setup/SETUP-mac.md`
   - Linux: `setup/SETUP-linux.md`

2. Install Python (recommended 3.10–3.12) and a virtual environment.

3. Install dependencies. This repository uses different tools in subprojects; a common starting point is:

```bash
pip install -r requirements.txt
```

Some examples use `uv` and `crewai` for dependency and project handling; see each subproject README for details.

4. Set required environment variables (examples):

```bash
export OPENAI_API_KEY="sk-..."
```

5. Run an example crew (from repo root):

```bash
# from repo root
crewai run
```

or open and run the Jupyter notebooks in the folders (use Jupyter or VS Code).

## Notebooks
Most of the repository content is in Jupyter notebooks. Open them with Jupyter Lab or VS Code for interactive exploration.

## Contributing
Contributions, bug reports and feature requests are welcome. Please open an issue describing your change and follow the code/styles in the repo.

## License
This project is distributed under the terms of the LICENSE file in the repository.

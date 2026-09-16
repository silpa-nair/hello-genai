# Copilot Instructions

- Important! Always follow the instructions in `./instructions/main.agent.md` file.
- Always load the file completely, not partially.
- It contains links to other files with instructions.
- You should reload it in **every prompt** to get the latest instructions - because of the dynamic nature of the project.

## Project conventions

- Python functions use short one-line docstrings (see [work/module03-task/calculator.py](../work/module03-task/calculator.py), [jira_status_report/jira_client.py](../jira_status_report/jira_client.py)).
- Secrets (API tokens, credentials) go in `.env` files, never committed; provide a matching `.env.example` with placeholder values.
- `work/module03-task/` is its own git repository, separate from the workspace root repo — check which repo a file belongs to before running git commands.
- Training module completion reports are saved under `work/` as `module-NN-report.md`.

## Git commits

- Stage only the file(s) explicitly requested for a commit — do not bulk-add unrelated untracked files.
- Git is installed at `C:\Program Files\Git\bin\git.exe` but not on PATH in this environment; invoke it via its full path in terminal commands.

## Documentation

- Do not create markdown documentation files unless explicitly requested.

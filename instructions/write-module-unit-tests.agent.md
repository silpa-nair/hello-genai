- Use this when asked to write unit tests for a Python module in this project (report builders, API clients, data-processing helpers).
- Input format:
  + The target module's file path and its public functions/classes to cover.
  + Any known edge cases already noted for that module (e.g. empty sprint, missing custom field, zero-activity contributor).
- Processing steps:
  + Identify every public function/method in the target module and list the distinct behaviors each one has (normal case, empty input, missing/None fields, boundary values).
  + For modules that call external APIs (Jira/Confluence clients), mock the HTTP layer (e.g. `requests` calls) — never make real network calls in unit tests.
  + Write one test function per distinct behavior; name tests `test_<function>_<scenario>`.
  + Use fixtures or small helper builders for repeated fake data (e.g. a fake issue dict) instead of duplicating literals across tests.
- Output format:
  + A `test_<module_name>.py` file colocated with the module under test, using `pytest` conventions (plain `assert` statements, no unittest boilerplate unless the project already uses it).
  + Group related tests with clear, descriptive names — no numbered or vague test names like `test_1`.
- Constraints:
  + Cover at minimum: the normal/happy path, an empty-input case, and any case explicitly called out in the module's backlog item (e.g. "empty-sprint case", "zero-activity contributor").
  + Do not test third-party library internals (e.g. `requests` itself) — only this project's logic.
  + Keep tests deterministic — no reliance on real dates/times or live API state; freeze/inject any time-dependent values.

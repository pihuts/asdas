# Final Prompt: AI-Optimized Research README Generator

> [!IMPORTANT]
> **System Role: Expert LLM-Oriented Documentation Generator**
>
> You are an expert in creating LLM-optimized, accurate, and maintainable documentation for software libraries and packages. Your analysis and output must be precise and derived solely from the provided project materials.

## Mission

Your mission is to read and analyze the provided project (source code, documentation, dependency files) and then produce a complete, self-contained, and LLM-friendly `README.md` file.

The goal is to enable any other LLM or autonomous agent to:
1.  Correctly install, configure, and use the library.
2.  Understand its key concepts, architecture, and idiomatic patterns.
3.  Follow clear, runnable examples of safe usage.
4.  Know the common pitfalls, anti-patterns, and mistakes to avoid.
5.  Learn from a step-by-step tutorial from zero to productive use.
6.  See the exact current dependencies and their versions.
7.  Integrate code following best practices for maintainability and readability.

### Core Instructions

- **Scan & Document Dependencies:** Analyze files like `requirements.txt`, `pyproject.toml`, or `package.json`. Document the findings in a `research/requirements_report.md` file and summarize them in the `README_LLM.md`.
- **Create Runnable Examples:** Write tested code examples with descriptive variable names, no hidden state, and explicit imports.
- **Document Pitfalls:** Clearly state **What to Avoid**. This section must include deprecated APIs, unsafe configurations, poor naming conventions, magic numbers, performance traps, and integration gotchas.
- **Maintain a Change Log:** Document breaking changes and version-specific instructions.
- **Write a Tutorial:** Create a `Tutorial` section to onboard a new user (human or LLM) from initial setup to productive use.
- **Adhere to the Template:** Follow the Markdown structure provided below precisely.
- **Save Outputs:**
    1.  Save the completed README as `research/README_LLM.md`.
    2.  Save the dependency scan as `research/requirements_report.md`.
- **Ensure Factual Accuracy:** ALL guidance must be derived from the project’s actual code and documentation. Do not fabricate functionality.
- **Maintain Consistency:** Ensure design consistency and integration coherence across all examples, as per the best practices for real-system code generation highlighted in [Code Generation with LLMs: Practical Challenges, Gotchas, and Nuances](https://medium.com/@adnanmasood/code-generation-with-llms-practical-challenges-gotchas-and-nuances-7b51d394f588).

> [!WARNING]
> You **MUST** ensure that any LLM reading the final `research/README_LLM.md` will:
> - Confidently know how to use the library/package without missing any steps.
> - Be fully aware of all known pitfalls and understand what **NOT** to do.

---

## Markdown Output Template
*(This is the structure you must fill in and output as `research/README_LLM.md`)*

```markdown
# {{Library Name}} (v{{Version}})

## Overview
{{Provide a concise summary of the library's purpose, scope, domain, and reason for existence.}}

## Installation

**Installation Command:**
```bash
{{The primary installation command, e.g., pip install -r requirements.txt}}
```

**Detected Requirements:**
```
{{Auto-generated list of dependencies and versions from project files}}
```

## Core Concepts

* **Main Modules:** {{A summary of the main modules and their responsibilities.}}
* **Key Classes/Functions:**
    * `ClassName`: {{Explanation of its role.}}
    * `function_name()`: {{Explanation of its role.}}
* **Important Terminology:**
    * `Term`: {{Definition.}}

## Quick Start Example

A runnable example demonstrating best-practice style.

```python
# Example: Clear, explicit configuration and execution
from {{main_module}} import {{primary_function_or_class}}

# Use descriptive names and explicit structures
db_connection_config = {
    "host": "localhost",
    "port": 5432,
    "user": "admin"
}

data_processor = {{primary_function_or_class}}(config=db_connection_config)
result = data_processor.run()

print(f"Processing finished with result: {result}")
```
> [!TIP]
> **Best Practices:**
> * Explicit is better than implicit.
> * Use descriptive variable names.
> * Avoid magic numbers; define constants instead.

## Advanced Usage

This example shows proper error handling and integration patterns.

```python
from {{main_module}} import {{utility_class}}, CustomError

try:
    with {{utility_class}}(config_path="prod.yaml") as tool:
        tool.configure()
        tool.execute_long_running_task()
except FileNotFoundError as e:
    print(f"ERROR: Configuration file not found at {e.filename}")
except CustomError as e:
    print(f"A library-specific error occurred: {e}")
```

## Tutorial

#### 1. Install
Run the following command in your terminal:
```bash
{{Exact installation command}}
```

#### 2. Initialize
Create a file `main.py` with the following minimal code to start using the library:
```python
{{Minimal, runnable "hello world" example}}
```

#### 3. Extend
Here is a common pattern for integrating the library into a larger application:
```python
{{Example showing integration, e.g., inside a function or class}}
```

#### 4. Test
Verify your setup is working correctly by running the provided tests:
```bash
{{Command to run tests, e.g., python -m unittest}}
```

## What to Avoid

* **Pitfall 1: Modifying Internal Attributes:** Do not directly modify attributes prefixed with an underscore (e.g., `obj._internal_state`). Use public methods instead.
* **Pitfall 2: Unsafe Configuration:** Avoid using default passwords or leaving sensitive keys in version control. Load them from environment variables.
* **Deprecated Functions:** Avoid using `deprecated_function()`; it will be removed in v2.0. Use `new_function()` instead.
* **Performance Traps:** Calling `process_item()` in a loop for thousands of items is inefficient. Use the batch method `process_batch()` instead.

## Troubleshooting

| Issue                     | Probable Cause                               | Solution                                                     |
| ------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| `AuthenticationError`     | Invalid or expired API credentials.          | Check your `.env` file and refresh your API token.           |
| `ModuleNotFoundError`     | A required dependency is not installed.      | Run `pip install -r requirements.txt` to install all dependencies. |

## Testing

A sample test case to verify core functionality.

```python
import unittest
from {{main_module}} import {{function_to_test}}

class Test{{LibraryName}}(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual({{function_to_test}}({{sample_input}}), {{expected_output}})

    def test_edge_case_handling(self):
        with self.assertRaises(ValueError):
            {{function_to_test}}({{invalid_input}})
```

## AI Agent Notes
{{This space is reserved for future AI agents to append clarifications, usage caveats, or observations based on code changes.}}

## Change Log

| Version | Date         | Key Changes                                                 |
| ------- | ------------ | ----------------------------------------------------------- |
| `1.1.0` | `YYYY-MM-DD` | Added `new_feature()`. Deprecated `old_feature()`.            |
| `1.0.0` | `YYYY-MM-DD` | **Breaking Change:** Migrated from `config.json` to `config.yaml`. |

```

---

### Expected Execution Output

When you run this prompt against a repository, you will generate the following file structure in the `research/` directory:

```
research/
├─ README_LLM.md        # The LLM-friendly, self-contained documentation you generated.
└─ requirements_report.md # An auto-extracted report of current dependencies.
```

### Rationale for this Approach

* **Structured Parsing:** Mirrors the **ReadMe.LLM** approach from [arXiv:2504.09798v3](https://arxiv.org/html/2504.09798v3) so LLMs can reliably parse the document.
* **Stateful Consistency:** Ensures multi-file, stateful project integration consistency as discussed in [this Medium article](https://medium.com/@adnanmasood/code-generation-with-llms-practical-challenges-gotchas-and-nuances-7b51d394f588).
* **Pitfall Awareness:** Embeds explicit warnings and anti-patterns so that models do not repeat known mistakes from the codebase.
* **Offline Utility:** Keeps all necessary information self-contained for use in isolated or offline AI code generation pipelines.
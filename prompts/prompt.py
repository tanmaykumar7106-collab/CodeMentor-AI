def build_test_case_prompt(code, language, coverage):
    return f"""
You are a software testing expert.

Analyze this {language} code and generate {coverage.lower()} test coverage.

Return the result as a Markdown table with these columns:

| ID | Category | Test Scenario | Input | Expected Output | Priority |

Include:
- Functional test cases
- Boundary test cases
- Edge cases
- Negative test cases

Rules:
- Do not write explanations before the table.
- Keep every test case on one table row.
- Priority must be High, Medium or Low.
- Expected outputs must follow the actual code logic.

Code:

{code}
"""
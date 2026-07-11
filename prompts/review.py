def build_review_prompt(code, language):
    return f"""
You are a programming instructor.

Review this {language} code for a student.

Provide:

1. Code Summary
2. What Is Done Well
3. Errors or Problems
4. Improvement Suggestions
5. Time Complexity
6. Space Complexity
7. Improved Code
8. Learning Tips

Use simple language and markdown headings.

Code:

{code}
"""
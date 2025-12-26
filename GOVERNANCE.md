# Governance Model

The **FinLab Coding Assistant** project aims to provide a standardized, high-quality knowledge base for Large Language Models (LLMs) to assist users in writing FinLab quantitative strategies.

## 1. Project Mission

Our mission is to ensure that AI assistants (like ChatGPT and Gemini) generate **accurate**, **executable**, and **idiomatic** FinLab Python code. We achieve this by maintaining a "Single Source of Truth" for API specifications and data definitions.

## 2. Roles and Responsibilities

### Maintainers
- Responsible for the overall direction of the project.
- Have the final say on changes to `document.md` and `database.md` to ensure they strictly align with the official FinLab platform.
- Review and merge Pull Requests.

### Contributors
- Can propose updates to documentation, style guides, or system prompts.
- Report issues or inaccuracies in AI responses caused by the knowledge base.

## 3. Decision Making Process

### Core Documentation (`document.md`, `database.md`)
- **Strict Adherence**: Changes to these files must be backed by official FinLab updates.
- **Verification**: Any new API or data field added must be verifiable on the FinLab platform.
- **Approval**: Requires Maintainer review to prevent "hallucinated" features from entering the knowledge base.

### Style Guide (`STYLE_GUIDE.md`)
- **Consensus**: Changes to coding styles (e.g., variable naming, structure) are open for discussion.
- **Goal**: The goal is readability and maintainability. We prefer conventions that align with the broader Python and Quant community.

### System Instructions (`*/SYSTEM_INSTRUCTION.md`)
- **Optimization**: We welcome prompt engineering improvements that make the AI smarter or more obedient.
- **Testing**: Changes should be tested across different models (GPT-4, Gemini 1.5 Pro) to ensure consistent performance.

## 4. Contribution Process

1.  **Fork & Branch**: Fork the repository and create a branch for your changes.
2.  **Edit**: Make your changes.
    - If updating `document.md`, please provide a reference link to the official doc.
3.  **Pull Request**: Submit a PR with a clear description of why the change is needed.
4.  **Review**: Maintainers will review the PR.

## 5. Code of Conduct

We are committed to providing a friendly, safe, and welcoming environment for all, regardless of level of experience, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, religion, nationality, or other similar characteristic.


import json
import re
from pathlib import Path


# Locate the project's skill dataset
PROJECT_ROOT = Path(__file__).resolve().parents[3]
SKILLS_FILE = PROJECT_ROOT / "data" / "skills.json"


def load_skills():
    """Load the skill knowledge base from JSON."""

    with open(SKILLS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def extract_skills(resume_text):
    """Extract recognized technical skills from resume text."""

    skills = load_skills()
    extracted = []

    for skill in skills:
        aliases = skill["aliases"]

        for alias in aliases:
            pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

            if re.search(pattern, resume_text, re.IGNORECASE):
                extracted.append({
                    "name": skill["name"],
                    "category": skill["category"]
                })
                break

    return extracted


if __name__ == "__main__":

    sample_resume = """
    I have experience in Java, Python, SQL and Machine Learning.
    I have worked with Pandas, NumPy, React, Flask and Git.
    """

    results = extract_skills(sample_resume)

    print("\nExtracted Skills:")

    for skill in results:
        print(f"{skill['name']} - {skill['category']}")

    print(f"\nTotal skills found: {len(results)}")
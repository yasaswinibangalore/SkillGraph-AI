
from backend.app.ml.skill_extractor import extract_skills


def analyze_job_description(job_description):
    """Extract technical skills from a job description."""

    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    skills = extract_skills(job_description)

    return {
        "total_required_skills": len(skills),
        "required_skills": skills
    }


if __name__ == "__main__":

    sample_job = """
    We are looking for a Software Engineer.

    Required skills:
    Java, Python, SQL, Spring Boot,
    REST APIs, Git, Data Structures,
    OOP and MongoDB.
    """

    analysis = analyze_job_description(sample_job)

    print("\n===== JOB DESCRIPTION ANALYSIS =====")
    print("Total Required Skills:",
          analysis["total_required_skills"])

    for skill in analysis["required_skills"]:
        print(f"{skill['name']} - {skill['category']}")
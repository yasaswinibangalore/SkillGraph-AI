
from backend.app.services.resume_parser import extract_text_from_pdf
from backend.app.ml.skill_extractor import extract_skills


def analyze_resume(pdf_path):
    """
    Read a PDF resume and extract technical skills.
    """

    # Step 1: Extract text from PDF
    resume_text = extract_text_from_pdf(pdf_path)

    # Step 2: Identify technical skills
    skills = extract_skills(resume_text)

    # Step 3: Prepare analysis result
    result = {
        "total_skills_found": len(skills),
        "skills": skills
    }

    return result


if __name__ == "__main__":

    resume_path = "data/sample_resumes/sample_resume.pdf"

    analysis = analyze_resume(resume_path)

    print("\n===== SKILLGRAPH AI RESUME ANALYSIS =====")

    print("\nTotal Skills Found:",
          analysis["total_skills_found"])

    print("\nExtracted Skills:")

    for skill in analysis["skills"]:
        print(
            f"{skill['name']} - {skill['category']}"
        )
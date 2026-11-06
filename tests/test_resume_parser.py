
from backend.app.services.resume_analyzer import analyze_resume


def test_complete_resume_analysis():

    result = analyze_resume(
        "data/sample_resumes/sample_resume.pdf"
    )

    assert isinstance(result, dict)

    assert "total_skills_found" in result
    assert "skills" in result

    assert result["total_skills_found"] > 0

    skill_names = [
        skill["name"] for skill in result["skills"]
    ]

    assert "Java" in skill_names
    assert "Python" in skill_names
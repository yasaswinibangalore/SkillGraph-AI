
from backend.app.ml.skill_extractor import extract_skills


def test_extract_java_and_python():
    text = "I know Java and Python."

    results = extract_skills(text)
    names = [skill["name"] for skill in results]

    assert "Java" in names
    assert "Python" in names


def test_extract_case_insensitive():
    text = "I have experience in JAVA and PYTHON."

    results = extract_skills(text)
    names = [skill["name"] for skill in results]

    assert "Java" in names
    assert "Python" in names


def test_no_skills_found():
    text = "I enjoy reading books and travelling."

    results = extract_skills(text)

    assert results == []


def test_no_duplicate_skills():
    text = "Python, python and PYTHON."

    results = extract_skills(text)
    names = [skill["name"] for skill in results]

    assert names.count("Python") == 1
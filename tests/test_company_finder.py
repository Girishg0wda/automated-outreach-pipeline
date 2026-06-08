from services.company_finder import find_similar_companies

def test_company_finder():
    result = find_similar_companies("openai.com")
    assert len(result) > 0
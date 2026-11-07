from src.rag import compare
def test_compare():
    d = compare("term net 30 days", "term net 45 days")
    assert "30" in d["only_a"] and "45" in d["only_b"]

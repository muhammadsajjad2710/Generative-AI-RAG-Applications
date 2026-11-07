from src.rag import fit_adapter
def test_adapter():
    pairs = [("reset password", "account"), ("invoice copy", "billing"), ("api 500", "tech")] * 10
    metrics = fit_adapter(pairs)
    assert metrics["accuracy"] >= 0.8

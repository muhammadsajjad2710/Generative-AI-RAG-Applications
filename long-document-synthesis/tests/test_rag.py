from src.rag import Store, answer_with_citations, ingest_long
def test_chunks():
    s = Store()
    ingest_long(s, "alpha " * 30 + " unique-token-zebra " + "beta " * 30)
    hits = s.search("unique-token-zebra")
    ans = answer_with_citations(hits, "zebra")
    assert "zebra" in ans["answer"]
    assert ans["citations"]

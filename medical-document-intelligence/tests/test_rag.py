from src.rag import Store, answer_with_citations, groundedness
def test_citations_and_groundedness():
    s = Store()
    s.add("guid-12", "Adults with fever should rest and hydrate unless red flags appear.")
    hits = s.search("fever rest")
    ans = answer_with_citations(hits, "fever")
    assert ans["citations"]
    assert groundedness(ans["answer"], hits) >= 0.5

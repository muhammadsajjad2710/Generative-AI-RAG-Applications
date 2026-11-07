from src.rag import Store
from src.rag import rerank, overlap
def test_rerank_improves_or_keeps_gold():
    s = Store()
    s.add("1", "cats sit on mats")
    s.add("2", "the quarterly budget process")
    s.add("3", "cat food and toys")
    hits = rerank("cat toys", s.search("cat toys", k=3))
    assert overlap([h.doc_id for h in hits[:2]], ["3", "1"]) >= 0.5

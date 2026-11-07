from pathlib import Path
from src.rag import Store, answer_with_citations, index_repo
def test_indexes_this_package():
    s = Store()
    index_repo(Path(__file__).resolve().parents[1] / "src", s)
    hits = s.search("class Store")
    ans = answer_with_citations(hits, "Store")
    assert ans["citations"]

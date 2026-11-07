from src.rag import Store
from src.rag import add_table, add_image
def test_multimodal():
    s = Store()
    s.add("d1", "Q4 revenue grew 12 percent.")
    add_table(s, "t1", ["sku,price", "MUG,4.99"])
    add_image(s, "i1", "photo of a ceramic mug on a shelf")
    hits = s.search("mug")
    ids = {h.doc_id for h in hits}
    assert "t1" in ids or "i1" in ids

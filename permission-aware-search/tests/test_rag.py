from src.rag import Store
def test_acl():
    s = Store()
    s.add("pub", "office wifi password is posted on the intranet banner")
    s.add("secret", "merger talks with Orion")
    hits = s.search("merger", allow={"pub"})
    assert all(h.doc_id != "secret" for h in hits)

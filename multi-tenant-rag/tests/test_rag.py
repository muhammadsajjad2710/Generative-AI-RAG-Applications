from src.rag import Store, answer_with_citations
def test_tenant_isolation():
    s = Store()
    s.add("a1", "Alpha payroll policy uses ADP.", tenant="alpha")
    s.add("b1", "Beta payroll policy uses Workday.", tenant="beta")
    hits = s.search("payroll policy", tenant="alpha")
    assert hits and all(h.tenant == "alpha" for h in hits)
    ans = answer_with_citations(hits, "payroll")
    assert "ADP" in ans["answer"]
    assert "Workday" not in ans["answer"]

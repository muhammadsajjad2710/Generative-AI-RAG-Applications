from src.rag import is_safe_sql, to_sql
def test_sql_guard():
    assert is_safe_sql(to_sql("show amounts"))
    assert not is_safe_sql("SELECT * FROM orders; DROP TABLE orders")
    assert not is_safe_sql("DELETE FROM orders")

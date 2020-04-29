def func(db_engine):
    query = f"SELECT * FROM table"
    query_result = db_engine.execute(query).fetchall()
    extracted_val = []
    for res in query_result:
        extracted_val.append(res[1])
    return extracted_va

def query_db(db_connection, query):
    cur = db_connection.cursor()
    try:
        print(f"Query to be executed : {query}")
        cur.execute(query)
        results = cur.fetchall()
        print(f"Query Results : {results}")
    except Exception:
        print("Exception while executing \'query_db\' function")
        raise Exception(
            f"Error while executing query : {query}. Please check the logs for details")
    return results

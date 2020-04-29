class A():
    def __init__(self, engine):
        self.engine = engine

    def fetch_data(self):
        with self.engine.begin() as trans:
            rval = trans.execute("SELECT * FROM XXX")

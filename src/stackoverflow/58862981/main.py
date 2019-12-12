class AADatabase:
    @classmethod
    def is_primary(cls):
        return False

    @classmethod
    def run(cls):
        return cls.is_primary()

class MyClass:
    def get_version(self):
        version = ''
        with open("file_path") as openfile:
            for line in openfile:
                sline = line.split()
                for row, column in enumerate(sline):
                    if column == "version=":
                        version = sline[row+1].strip('"')

        return version

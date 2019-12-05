import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/test.txt') as fp:
    src = fp.read(60)

print(len(src))
print(fp)
print(fp.closed, fp.encoding)
fp.read(60)

# python-codelab

Learning Python by examples

## Usage

To begin using the virtual environment, it needs to be activated:

```bash
source ./venv/bin/activate
```

deactivate virtual environment:

```bash
deactivate
```

Run test cases and generate test coverage report:

```bash
(venv) ☁  python-codelab [master] ⚡  coverage run /Users/ldu020/workspace/github.com/mrdulin/python-codelab/src/stackoverflow/54841363/test_content_provider.py && coverage report -m
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Name                                                  Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------
src/stackoverflow/54841363/content_provider.py            8      2    75%   3-4
src/stackoverflow/54841363/test_content_provider.py      11      0   100%
-----------------------------------------------------------------------------------
TOTAL                                                    19      2    89%
```

coverage include pattern:

```bash
coverage run /Users/ldu020/workspace/github.com/mrdulin/python-codelab/src/stackoverflow/60680124/test_employee.py && coverage report -m --include="src/*"
```

List global(system-level) pakcages:

```bash
☁  python-codelab [master] ⚡  pip3 list
Package          Version
---------------- ----------
certifi          2019.11.28
pip              19.3.1
pipenv           2018.11.26
setuptools       41.6.0
virtualenv       16.7.8
virtualenv-clone 0.5.3
wheel            0.33.6
```

List virtual environment(project-level) packages:

```bash
source .venv/bin/activate
pip3 list
```

Install packages in virtual environment via `requirements.txt` file:

```bash
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

Install packages ignore certificate issue:

```bash
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1076)'))': /simple/pillow/
```

```bash
pip3 install Pillow -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com/pypi
```

Use pytest with coverage report:

```bash
coverage run -m pytest /Users/ldu020/workspace/github.com/mrdulin/python-codelab/src/stackoverflow/53856568/test_code_53856568.py && coverage report -m --include="src/*"
```

## References

- [Proposal for a yield from statement for Python](http://www.cosc.canterbury.ac.nz/greg.ewing/python/yield-from/yield_from.html)
- [Effective Python: Second Edition — Source Code and Errata for the Book](https://github.com/bslatkin/effectivepython)
- [[Tutor] Comparing two CSV filess using Python](https://mail.python.org/pipermail/tutor/2015-February/104200.html)
- [Iterables, Iterators and Generators](https://nbviewer.jupyter.org/github/wardi/iterables-iterators-generators/blob/master/Iterables,%20Iterators,%20Generators.ipynb)
- [[Python-Dev] PEP 380 (yield from a subgenerator) comments](https://mail.python.org/pipermail/python-dev/2009-March/087382.html)
- [PEP 492 -- Coroutines with async and await syntax](https://www.python.org/dev/peps/pep-0492/)
- [simpy](https://pypi.org/project/simpy/)
- [Threads, processes and concurrency in Python: some thoughts](https://www.artima.com/weblogs/viewpost.jsp?thread=299551)
- [Example code for the book Fluent Python](https://github.com/fluentpython/example-code)
- [Embarrassingly parallel](https://en.wikipedia.org/wiki/Embarrassingly_parallel)
- [Coroutines and Tasks](https://docs.python.org/3.8/library/asyncio-task.html)
- [Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html)
- [Fan-in and Fan-out: The crucial components of concurrency](https://www.youtube.com/watch?v=CWmq-jtkemY)
- [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
- [unit testing with asyncio](http://jacobbridges.github.io/post/unit-testing-with-asyncio/)
- [virtualenvs](https://docs.python-guide.org/dev/virtualenvs/)

## Resources

- [Vaurien](https://vaurien.readthedocs.io/en/1.8/)
- [Pypy](https://www.pypy.org/)

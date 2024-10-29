from setuptools import setup

name = "types-s2clientprotocol"
description = "Typing stubs for s2clientprotocol"
long_description = '''
## Typing stubs for s2clientprotocol

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`s2clientprotocol`](https://github.com/Blizzard/s2client-proto) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `s2clientprotocol`. This version of
`types-s2clientprotocol` aims to provide accurate annotations for
`s2clientprotocol==5.*`.

Partially generated using [mypy-protobuf==3.6.0](https://github.com/nipunn1313/mypy-protobuf/tree/v3.6.0) and libprotoc 27.2 on [s2client-proto 5.0.12.91115.0](https://github.com/Blizzard/s2client-proto/tree/c04df4adbe274858a4eb8417175ee32ad02fd609).

This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/s2clientprotocol`](https://github.com/python/typeshed/tree/main/stubs/s2clientprotocol)
directory.

This package was tested with
mypy 1.13.0,
pyright 1.1.386,
and pytype 2024.10.11.
It was generated from typeshed commit
[`e92f98ccdaa6e06eb1260e9818590adc0dc8f223`](https://github.com/python/typeshed/commit/e92f98ccdaa6e06eb1260e9818590adc0dc8f223).
'''.lstrip()

setup(name=name,
      version="5.0.0.20241029",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/s2clientprotocol.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-protobuf'],
      packages=['s2clientprotocol-stubs'],
      package_data={'s2clientprotocol-stubs': ['build.pyi', 'common_pb2.pyi', 'data_pb2.pyi', 'debug_pb2.pyi', 'error_pb2.pyi', 'query_pb2.pyi', 'raw_pb2.pyi', 'sc2api_pb2.pyi', 'score_pb2.pyi', 'spatial_pb2.pyi', 'ui_pb2.pyi', 'METADATA.toml']},
      license="Apache-2.0",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)

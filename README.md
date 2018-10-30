# pybuf
Modularize Protocol Buffer Compiler generated code for use within your package.

### Version
v1.1.1


### Installation
```sh
pip install pybuf
```


### Quickstart
```python
from pybuf import modularize


modularize(source='/path/to/proto/files/directory/', destination='/path/to/module/', filename='specific_file.proto')
# filename param is optional
```


### Development
Want to contribute? Great! Fork and submit a pull request!
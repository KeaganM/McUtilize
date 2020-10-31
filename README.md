# McUtilize

A module with generic utility packages for various tasks. Currently the modules features the following:

* file_ops: a package dedicated for generic file operations
    1. standard_path: Function to standardize path (i.e. ./test/ = ./test)
    2. create_path: Create directories (including nested)
    3. get_desired_paths: Get a list of desired paths based on a path mapping (will find all cases)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install from github or install from wheel.

```bash
pip install git+https://github.com/KeaganM/McUtilize.git
```

## Usage

```python
import file_ops

path = './test/nested_test/nested_nested_test'

path_mapping = {
    'test_1':'.*test_1.*',
    'test_2':'.*test_2.*.shp'
}

 # standardize path
standard_path = file_ops.standardize_path(path)

# create full directory 
file_ops.create_path(standard_path) 

# get list of desired paths based on a directory and a path mapping
desired_paths = file_ops.get_desired_paths(path,path_mapping) 
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
import errno
import subprocess
from os.path import abspath
from os.path import exists
from os.path import join
from os import chmod
from os import listdir
from os import mkdir
from shutil import rmtree
from stat import S_IWRITE


init_filename = '__init__.py'


def modularize(source, destination, filename=None):
    """
    This method will call protoc on all proto files in <source> directory to generate
    the python code to encode/decode protobuf definitions

    :param source: Directory containing .proto files (Required)
    :param destination: Directory where generated python modules will be saved (Required)
    :param filename: Specific proto file to be call protoc on (Optional)
    """
    source = abspath(source)
    destination = abspath(destination)

    def rm_readonly(func, path, _):
        """
        Clear readonly and retry rmtree
        """
        chmod(path, S_IWRITE)
        func(path)

    # Remove destination directory if necessary
    try:
        rmtree(path=destination, onerror=rm_readonly)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise

    # Create destination directory
    mkdir(destination)

    if filename:
        cmd = 'protoc --python_out={} {}'.format(destination, filename)
    else:
        cmd = 'protoc --python_out={} *.proto'.format(destination)

    subprocess.call(cmd, shell=True, cwd=source)

    if filename:
        proto_files = [filename]
    else:
        proto_files = listdir(source)
    modules = []

    for name in proto_files:
        if name.endswith('proto'):
            filename = name.split('.')[:-2]
            if len(filename) > 0:
                modules.append(join(*filename))

    directory = destination
    open(join(directory, init_filename), 'w').close()
    for module in modules:
        if not exists(join(directory, module, init_filename)):
            open(join(directory, module, init_filename), 'w').close()
            subprocess.call('cp -r {} .'.format(join(directory, module)), shell=True)

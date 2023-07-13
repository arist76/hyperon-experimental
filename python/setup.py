import os
import shutil
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class CopyExtension(Extension):

    def __init__(self, name, source_dir='.', **kwa):
        Extension.__init__(self, name, sources=[], **kwa)
        self.source_dir = os.path.abspath(source_dir)

class CopyBuild(build_ext):

    def build_extensions(self):
        for ext in self.extensions:
            target_path = os.path.abspath(self.get_ext_fullpath(ext.name))
            ext_filename = os.path.basename(target_path)
            source_path = os.path.join(ext.source_dir, ext_filename)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.copyfile(source_path, target_path)

setup(
    ext_modules=[ CopyExtension('hyperonpy') ],
    cmdclass={ 'build_ext': CopyBuild },
)
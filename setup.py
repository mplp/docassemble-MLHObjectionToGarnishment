import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.MLHObjectionToGarnishment',
      version='0.0.1',
      description=('A Docassemble tool to create forms to object to garnishment in Michigan.'),
      long_description='# docassemble.MLHObjectionToGarnishment\n\nA Docassemble tool to create forms to object to garnishment in Michigan.\n\n## Author\n\nEmily Miller, ekressmiller@lsscm.org\n\n',
      long_description_content_type='text/markdown',
      author='Emily Miller',
      author_email='ekressmiller@lsscm.org',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_namespace_packages(),
      install_requires=['docassemble.AssemblyLine @ git+https://github.com/suffolklitlab/docassemble-assemblyline.git@main', 'docassemble.demo>=1.7.4', 'docassemble.mlhframework @ git+https://github.com/mplp/docassemble-mlhframework.git@main'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/MLHObjectionToGarnishment/', package='docassemble.MLHObjectionToGarnishment'),
     )


#!/usr/bin/env python3

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

with open('README.rst', encoding='utf-8') as file:
    readme = file.read()

class custom_build_ext(build_ext):
    def build_extensions(self):
        for extension in self.extensions:
            # -g0:
            #   Level 0 produces no debug information at all. This reduces
            #   the size of GCC wheels. By default CPython won't print any
            #   C stack trace, so -g0 and -g2 are same for most users.
            extension.extra_compile_args.append('-g0')
        super().build_extensions()

setup(
    name='clock_time',
    version='1.0',
    description=("Provide sleep(secs)/time_s() functions"),
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Ma Lin',
    author_email='malincns@163.com',
    url='https://bitbucket.org/wjssz/clock_time',
    license='The 3-Clause BSD License',
    python_requires='>=3.0',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: 3"
    ],
    keywords='sleep',

    package_dir={'clock_time': 'src'},
    packages=['clock_time'],
    package_data={'clock_time': ['__init__.pyi', 'py.typed']},

    ext_modules=[Extension('clock_time._clock_time',
                           ['src/_clock_time.c'])],
    cmdclass={'build_ext': custom_build_ext},
)
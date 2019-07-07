from setuptools import setup, find_packages

setup(
    name='packed_code',
    version='0.1.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='KatlegoM EDSA python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/katlegomfx/packed_code.git',
    author='katlegomfx',
    author_email='katlegomfx@gmail.com'
)

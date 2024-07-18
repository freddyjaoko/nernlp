from setuptools import setup, find_packages

setup(
    name='optimusnlp',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['data/ner.txt'],
    },
    description='A package for Named Entity Recognition',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/freddyjaoko/nernlp',
    author='Sam hiu',
    author_email='0z1yy6bfg@mozmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

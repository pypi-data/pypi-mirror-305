from setuptools import setup, find_packages

setup(
    name='aiomatter',
    version='0.1.0',
    author='Vladimir Savelev',
    author_email='ruslawsav@gmail.com',
    description='Mattermost async bot',
    long_description=open('README.MD').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/savvlex/aiomatter',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'websockets>=13.1',
        'pydantic>=2.9.2',
    ],
    python_requires='>=3.11',
)

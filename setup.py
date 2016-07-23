from setuptools import setup, find_packages

setup(
    name='python-cli-template',
    version="0.0.1",
    description='Python CLI template',
    author='sotetsuk',
    url='https://github.com/sotetsuk/python-cli-template',
    author_email='sotetsu.koyamada@gmail.com',
    license='MIT',
    install_requires=["docopt>=0.6.2"],
    packages=find_packages(),
    entry_points={
        'console_scripts': 'somecommand = somecommand.main:main'
    },
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License"
    ]
)

from setuptools import setup, find_packages

setup(
    name="com.hayatapps.pa.service.api",
    version="0.11",
    author="Roman Połchowski",
    author_email="rp@hayatapps.com",
    description="PA proto package",
    packages=find_packages(),
    install_requires=[
        'protobuf>=5.26.1',
        'grpcio>=1.56.2',
        'grpcio-tools>=1.56.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
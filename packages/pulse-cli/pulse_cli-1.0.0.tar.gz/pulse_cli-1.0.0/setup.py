from setuptools import setup, find_packages

setup(
    name='pulse-cli',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'pulse=pulse_cli.cli:main',
        ],
    },
    author='Petrobench',
    author_email='support@petrobench.com',
    description='A cross-platform CLI tool for managing the Pulse service',
    url='https://your-repository-url.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)

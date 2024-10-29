from setuptools import setup, find_packages

setup(
    name='scikit_learnt',  # The package name as you'd like it to be installed
    version='0.1.1',
    packages=find_packages(),
    install_requires=['openai==0.28.0'],  # Include dependencies here
    description='',
    author='Shaheer',
    author_email='shaheerzk01@gmail.com',
    url='https://github.com/username/scikit_learns',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

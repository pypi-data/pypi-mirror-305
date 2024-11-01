from setuptools import setup, find_packages

setup(
    name='fastapi-project-generator',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=7.0',
        'jinja2>=2.10',
    ],
    entry_points='''
        [console_scripts]
        fastapi-init=fastapi_project_generator.cli:main
    ''',
    author='Nirodya Pussadeniya',
    author_email='nirodya@synacal.ai',
    description='A package to generate FastAPI project structures.',
    url='https://github.com/Synacal/fastAPI-project-template.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: FastAPI',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

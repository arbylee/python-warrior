from setuptools import setup, find_packages


setup(
    name='pythonwarrior',
    version='0.0.8',
    packages=find_packages(),
    package_data={'pythonwarrior': ['templates/README']},
    scripts=['bin/pythonwarrior'],
    author="Richard Lee",
    author_email="rblee88@gmail.com",
    description=("Game written in Python for learning Python and AI - "
                 "a Python port of ruby-warrior"),
    long_description=open('README.rst').read(),
    install_requires=['jinja2'],
    license="MIT",
    url="https://github.com/arbylee/python-warrior",
    keywords="python ruby warrior rubywarrior pythonwarrior",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
    ]
)

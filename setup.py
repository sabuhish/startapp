from setuptools import setup
version = __import__("takeawy").__version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="startapp",
    version="0.0.1",
    py_modules=["colors"],
    include_package_data=True,
    version=version,
    author_email="",
    description="Simple startapp for flask dajngo and fastapo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/marlin-dev/",
    # scripts=['.py'],
    install_requires=[
        "click",
        "virtualenv"
    ],
    extras_require={
        "prompt_toolkit": ["prompt_toolkit == 1.0.14"]
    },
    entry_points="""
        [console_scripts]
        colors=takeaway.controllers.commands:BaseCommand
    """,
)






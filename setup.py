from setuptools import setup, find_packages
# version = __import__("takeaway").__version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="startapp",
    version="0.1.0",
    py_modules=["colors"],
    include_package_data=True,
    # version=version,
    packages=find_packages(),
    author_email="",
    description="Simple startapp for flask dajngo and fastapi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/marlin-dev/",
    # scripts=['.py'],
    install_requires=[
        "click"
    ],
    extras_require={
        "prompt_toolkit": ["prompt_toolkit == 1.0.14"]
    },
    entry_points="""
        [console_scripts]
        order=takeaway.script.order:cli
    """,
)









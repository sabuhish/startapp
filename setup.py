from setuptools import setup, find_packages
# version = __import__("takeaway").__version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="startapp",
    version="0.1.3.8e",
    include_package_data=True,
    packages=find_packages(),
    author="",
    author_email="",
    description="Simple startapp for fastapi flask  and django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/marlin-dev/startapp",
    install_requires=[
        "click"
    ],
    extras_require={
        "prompt_toolkit": ["prompt_toolkit == 1.0.14"]
    },
    entry_points="""
        [console_scripts]
        startapp=startapp.takeaway.script.order:starting
    """,
    # entry_points={
    #     'console_scripts': [
    #         'startapp=takeaway.script.order:cli
    #     ]
    # },

)









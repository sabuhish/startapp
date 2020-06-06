from setuptools import setup, find_packages
# version = __import__("takeaway").__version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="startapp",
    version="0.1.4.28",
    include_package_data=True,
    packages=['takeaway', 'takeaway.script','takeaway.core.utils','takeaway.core','takeaway.settings','takeaway.controllers','takeaway.settings.flask','takeaway.settings.fastapi','takeaway.settings.django'],
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
        startapp=takeaway.script.order:cli
    """,
    # entry_points={
    #     'console_scripts': [
    #         'startapp=takeaway.script.order:cli
    #     ]
    # },

)









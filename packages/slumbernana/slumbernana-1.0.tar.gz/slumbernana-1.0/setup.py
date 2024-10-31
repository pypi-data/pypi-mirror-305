from setuptools import setup, find_packages

setup(
    name='slumbernana',
    version='1.0',
    author='白狐不白',
    author_email='shk3210a@gmail.com',
    description="你，知道「睡蕉小猴」嗎？ 什麼？你不知道？那你有福了蕉！",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
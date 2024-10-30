import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="gdjd2l",
    version="0.1.1",
    author="Goodongj",
    author_email="",
    description="use for deep to learn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pythonml/douyin_image",
    packages=setuptools.find_packages(),
    install_requires=['torch>=2.3.1', 'numpy','pandas'],
    # entry_points={
    #     'console_scripts': [
    #         'douyin_image=douyin_image:main'
    #     ],
    # },
    # classifiers=(
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ),
)
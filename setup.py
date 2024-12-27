from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Pranay Kk",
    author_email="pranaykrishna1143@gmail.com",
    install_requires=["openai","langchain","streamlit","python_dotenv","PyPDF2"],
    packages=find_packages()
)
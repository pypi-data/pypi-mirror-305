from setuptools import setup, find_packages

setup(
    name='Mohit_SpeechToTextConverter',
    version='0.1',
    author='Mohit Kumar',
    author_email='megamohit2006@gmail.com',
    description='This is a speech-to-text package created by Mohit Kumar',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'webdriver_manager'
    ],
    include_package_data=True,
    package_data={
        'Mohit_SpeechToText': ['index.html', 'script.js', 'style.css', 'input.txt'],  # Include all necessary files
    },
)

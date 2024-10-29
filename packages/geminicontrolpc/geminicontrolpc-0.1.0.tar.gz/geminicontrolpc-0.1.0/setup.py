from setuptools import setup, find_packages

setup(
    name='geminicontrolpc',
    version='0.1.0',
    author='Trey Leonard',
    author_email='allanleonardiii@gmail.com',
    description='A Python package for controlling your PC using Google Gemini AI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gigachadtrey/geminicontrolpc',  # Update with your GitHub URL
    packages=find_packages(),
    install_requires=[
        'google-generativeai',
        'Pillow',
        'pygetwindow',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

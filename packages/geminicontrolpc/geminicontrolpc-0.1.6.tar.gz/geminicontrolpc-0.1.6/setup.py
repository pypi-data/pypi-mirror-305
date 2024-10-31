from setuptools import setup, find_packages

setup(
    name='geminicontrolpc',
    version='0.1.6',
    author='Trey Leonard',
    author_email='allanleonardiii@gmail.com',
    description='A Python package for controlling your PC using Google Gemini AI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gigachadtrey/geminicontrolpc',  # Your GitHub URL
    packages=find_packages(),
    install_requires=[
        'google-generativeai>=0.1.0',  # Specify a minimum version
        'Pillow>=8.0.0',                # Specify a minimum version
        'opencv-python>=4.0.0',         # Required for image capture if using OpenCV
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'geminictrlpc=geminicontrolpc.geminicontrolpc:main',  # Adjust this to match the main function in geminicontrolpc.py
        ]
    },
)

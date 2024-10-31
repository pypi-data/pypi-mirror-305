from setuptools import setup, find_packages

setup(
    name='thinklabs-powerflow',
    version='0.2.1',
    description='A CLI tool to process active and reactive power files and send them for power flow analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Suren Vallabhajosyula',
    author_email='suren.vallabhajosyula@thinklabs.ai',
    url='https://github.com/thinklabs-ai/thinklabs-powerflow-package.git',  # Update this if you have a GitHub repo
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
        'pandas',
        'certifi',
        'psycopg2-binary',
        'boto3',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'thinklabs-powerflow=thinklabs_powerflow.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)

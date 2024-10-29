from setuptools import setup, find_packages

setup(
    name='autocheck_plankin',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    project_urls={},
    entry_points={
        'console_scripts': [
            'autocheck=autocheck.__main__:main'
        ]
    },
    description='Перевод чека json в чек txt',
    author='Kirill'
)


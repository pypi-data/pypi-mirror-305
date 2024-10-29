from setuptools import setup, find_packages

setup(
    name='calculadora_lib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['pandas'],  # Dependências da biblioteca
    description='Uma biblioteca de exemplo para manipulação de dados',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Seu Nome',
    author_email='seu_email@example.com',
    url='https://github.com/seu_usuario/minha_biblioteca',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
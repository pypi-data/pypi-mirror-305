from setuptools import setup, find_packages

setup(
    name='validacoes_usuarios',
    version='1.0.0',
    description='Biblioteca para validação de senha e e-mail para segurança de dados dos usuários.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Seu Nome',
    author_email='seuemail@example.com',
    url='https://github.com/AlaiSeide/validacoes_usuarios.git',  # Link para o repositório GitHub
    packages=find_packages(),
    install_requires=[
        'wtforms',
        'dnspython',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
)

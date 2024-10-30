from setuptools import setup, find_packages

setup(
    name='mi_plugin_de_fechas',                   
    version='0.1.0',                              
    description='Un plugin para convertir fechas según código postal',
    long_description=open('README.md').read(),    
    long_description_content_type='text/markdown',
    author='Pedro Saldana',                           
    author_email='psaldana@businessdebtadjusters.com',           
    url='https://github.com/tuusuario/mi_plugin_de_fechas',  
    packages=find_packages(),                     
    install_requires=[
        'pytz>=2024.1',                           
    ],
    classifiers=[                                 
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                      
)

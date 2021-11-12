from setuptools import setup

setup(
    name='remoteobjects-py',
    version='0.1.0',    
    description='Python Remote Objects wrapper',
    url='https://github.com/prakis/remoteobjects-py',
    author='Kishore',
    author_email='prakis@gmail.com',
    license='MIT',
    packages=['remoteobjects-py'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
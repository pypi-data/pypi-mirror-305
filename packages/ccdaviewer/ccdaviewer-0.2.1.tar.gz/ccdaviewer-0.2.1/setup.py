from distutils.core import setup

setup(
    name = 'ccdaviewer',     
    packages = ['ccdaviewer'],  
    version = '0.2.1', 
    license='MIT',      
    description = 'This is the python client to the API hosted by https://www.ccdaviewer.com', 
    author = 'Tanaka Chiromo',                   
    author_email = 'tanakachiromo@gmail.com',   
    url = 'https://github.com/tanaka-chiromo/ccdaviewer',  
    download_url = 'https://github.com/tanaka-chiromo/ccdaviewer/archive/refs/tags/v_021.tar.gz',
    keywords = ['ccdaviewer', 'API', 'Client'],  
    install_requires=[      
            'requests'
        ],
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    )
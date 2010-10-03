from distutils.core import setup
setup(
    name='concordar',
    version='0.1alpha',
    description='A simple GUI tool for building concordances',
    long_description='A simple GUI tool for building concordances',
    license='GNU GPL v3',
    author='Ludovico Fischer',
    author_email='livrerie@gmail.com',
    url='http://github.com/ludovicofischer/concordar',
    package_dir={'': 'concordar'},
    py_modules=['concordance', 'texttools','ui_main_window', 'models'],
    scripts=['concordar.py'],
    requires=['PyQt4',]
)
    
    

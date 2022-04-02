from setuptools import setup

setup(name='tone-clock-diagram',
      version='1.0',
      author='Saleem Khair',
      author_email='saleemkhair@gmail.com',
      url='https://github.com/SaleemKhair/tone-clock-diagram',
      package_dir={
          'model': './src/model',
          'serialization': './src/serialization',
          'controller': './src/controller',
          'server': './src/server'
      },
      packages=['model', 'serialization', 'controller', 'server'],
      )

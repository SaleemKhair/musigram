from setuptools import setup, find_packages

setup(name='musigram',
      description='''
        Library to translate MIDI signals into pitch-class sets or tone-clock sets,
        and provide basic post-tonal analysis operations.
      ''',
      version='1.0',
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: Apache License 2.0',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Music',
          'Topic :: Math',
      ],
      license='Apache License 2.0',
      author='Saleem Khair',
      platforms=['POSIX'],
      author_email='saleemkhair@gmail.com',
      url='https://github.com/SaleemKhair/tone-clock-diagram',
      python_requires='>= 3.8.10',
      install_requires=[
          'mido >= 1.2.10',
          'JACK-Client >= 0.5.3',
          'python-rtmidi >= 1.4.9',
          'pulsectl >= 22.3.2',
          'coloredlogs >= 15.0.1',
          'pyyaml >= 6.0'
      ],
      packages=find_packages(exclude='tests'),
      scripts=['bin/proc_clock_vermidi']
      )

from setuptools import setup
setup(name='roadtune',
      version='0.0.1',
      description='ROADtools Intune client',
      author='Dirk-jan Mollema',
      author_email='dirkjan@outsidersecurity.nl',
      url='https://github.com/dirkjanm/ROADtools/',
      license='MIT',
      classifiers=[
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
      ],
      packages=['roadtools.roadtune'],
      install_requires=[
          'roadlib>=0.23',
          'requests',
          'oscrypto'
      ],
      zip_safe=False,
      include_package_data=True,
      entry_points={
          'console_scripts': ['roadtune=roadtools.roadtune.main:main',]
      }
      )

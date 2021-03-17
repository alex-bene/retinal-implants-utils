from distutils.core import setup

setup(
  name = 'retinal_implants_utils',
  packages = ['retinal_implants_utils'],
  version = '0.0.2',
  license='MIT',
  description = 'Utilities to help with retinal implants simulation and evaluation',
  author = 'Alexandros Benetatos',
  author_email = 'alexandrosbene@gmail.com',
  url = 'https://github.com/alex-bene/retinal-implants-utils',
  download_url = 'https://github.com/alex-bene/retinal-implants-utils/archive/v0.0.2-beta.tar.gz',
  keywords = ['retinal implants', 'pulse2percept', 'utilities'],
  install_requires=[
          'tqdm',
          'numpy',
          'torch',
          'pillow',
          'pickle',
          'scikit-image',
          'matplotlib',
          'pytorchUtils==0.0.3',
          'pulse2percept==0.7.0',
                   ],
  classifiers=[
    'Development Status :: 4 - Beta', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
              ],
)

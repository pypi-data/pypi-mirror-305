from setuptools import setup, find_packages

classifiers = [
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Operating System :: OS Independent',
	'Programming Language :: Python :: 3'
]

setup(
	name='pyshooter2d',
	version='0.0.4',
	description='a package for faster and easier development of 2d shooters',
	long_description=open('README.txt').read() + '\n' + open('CHANGELOG.txt').read(),
	author='Freddy Frolov',
	author_email='freddyfrolov383@gmail.com',
	license='MIT',
	classifiers=classifiers,
	packages=find_packages(),
	keywords='shooter engine',
	install_requires=['pygame-ce', 'math']
)
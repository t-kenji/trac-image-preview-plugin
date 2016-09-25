from setuptools import find_packages, setup

version='0.1'

setup(
    name='TracImagePreviewPlugin',
    url='https://github.com/t-kenji/trac-image-preview-plugin',
    long_description='Image preview for Trac',
    author='t-kenji',
    author_email='protect.2501@gmail.com',
    version=version,
    license = 'BSD', # the same as Trac

    install_requires = ['Trac >= 1.0'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    entry_points = {
        'trac.plugins': [
            'tracimagepreview = tracimagepreview'
        ]
    }
)

import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'rapport'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='Misty robot ROS2 package for CCR Scale Study 3',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'publisher_text = rapport.MistyGUI:main',
        'subscriber_text = rapport.MistySubscriber:main',
        'slides = rapport.SlidesSubscriber:main'
        ],
    },
)

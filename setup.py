# Copyright (c) 2024 Touchlab Limited. All Rights Reserved
# Unauthorized copying or modifications of this file, via any medium is strictly prohibited.

import os
from glob import glob
from setuptools import find_packages, setup

__version__ = "0.1.4"
package_name = 'touchlab_driver_ros'

setup(
    name=package_name,
    version=__version__,
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    zip_safe=True,

    author="Vladimir Ivan",
    author_email="vlad@touchlab.com",
    license='Touchlab Limited',
    description="Touchlab Sensor ROS Driver",
    python_requires=">=3.8",
    scripts=['scripts/touchlab_driver',],
)
from setuptools import find_packages, setup

package_name = 'dynamixelAx12'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adrien',
    maintainer_email='adrien.pouxviel@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bluetooth_receiver = dynamixelAx12.bluetooth_receiver:main',
            'motor_controller = dynamixelAx12.motor_controller:main' 

        ],
    },
)

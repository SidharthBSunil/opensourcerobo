from setuptools import find_packages, setup

package_name = 'raju_brain'

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
    maintainer='sidharth',
    maintainer_email='sidharth@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
	'raju_brain = raju_brain.brain_node:main',
	'hand_servo_publisher = raju_brain.hand_servo_publisher:main',
        ],
    },
)

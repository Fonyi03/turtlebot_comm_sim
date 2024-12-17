from setuptools import find_packages, setup

package_name = 'turtlebot_comm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fonyo',
    maintainer_email='fonyo.mate@hallgato.sze.hu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'communication_node = turtlebot_comm.communication_node:main',
            'subscriber_node = turtlebot_comm.subscriber_node:main',
            'topic_publisher = turtlebot_comm.topic_publisher:main',
        ],
    }
)

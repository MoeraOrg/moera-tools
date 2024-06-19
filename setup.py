from setuptools import setup

setup(
    name='moera-tools',
    version='0.3.1',
    install_requires=[
        'moeralib~=0.15.3',
        'python-dateutil',
        'PyYAML',
        'first',
        'docopt',
        'cryptography~=42.0.4',
        'mnemonic'
    ],
)

from setuptools import setup, find_packages

setup(
    name="PhasorialCircuit",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.1",
        "schemdraw>=0.19",
    ],
    url = 'https://github.com/ygordealmeida/Phasorial_Circuit_Simulator/tree/module-archives',
    author="@ygordealmeida",
    description="Circuits simulation in phasorial domain",
)

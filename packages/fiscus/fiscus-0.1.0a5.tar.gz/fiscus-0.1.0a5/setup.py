import sys
import glob
import os
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
from distutils.errors import CompileError
from Cython.Build import cythonize

# Custom build_ext command to check for C compiler
class BuildExt(build_ext):
    def run(self):
        try:
            # Attempt to run the build process
            super().run()
        except CompileError as e:
            # If there's a compilation error, print a helpful message
            print("*****************************************************************")
            print("ERROR: A C compiler is required to build this package from source.")
            print("Please install a C compiler or try installing a pre-built wheel.")
            print("*****************************************************************")
            sys.exit(1)

# Collect all .pyx files in the src/fiscus directory for Cython compilation
module_paths = glob.glob("src/fiscus/*.pyx")

# Create an Extension object for each module (e.g., 'fiscus.module_name')
extensions = [
    Extension(
        # Module name (e.g., 'fiscus.module_name')
        "fiscus." + os.path.splitext(os.path.basename(path))[0],
        [path],
    )
    for path in module_paths
]

# Read the long description from README.md to use in setup metadata
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()
    
# List of core dependencies (required packages with minimum versions)
install_requires = [
    'aiohappyeyeballs>=2.4.3',
    'aiohttp>=3.10.10',
    'aiosignal>=1.3.1',
    'annotated-types>=0.7.0',
    'anyio>=4.6.2.post1',
    'attrs>=24.2.0',
    'certifi>=2024.8.30',
    'charset-normalizer>=3.4.0',
    'distro>=1.9.0',
    'filelock>=3.16.1',
    'frozenlist>=1.4.1',
    'fsspec>=2024.9.0',
    'gevent>=24.2.1',
    'greenlet>=3.1.1',
    'h11>=0.14.0',
    'httpcore>=1.0.6',
    'httpx>=0.27.2',
    'idna>=3.10',
    'jiter>=0.6.1',
    'multidict>=6.1.0',
    'packaging>=24.1',
    'propcache>=0.2.0',
    'pydantic>=2.9.2',
    'pydantic_core>=2.23.4',
    'PyYAML>=6.0.2',
    'requests>=2.32.3',
    'setuptools>=75.1.0',
    'sniffio>=1.3.1',
    'tqdm>=4.66.5',
    'typing_extensions>=4.12.2',
    'urllib3>=2.2.3',
    'websocket-client>=1.8.0',
    'websockets>=13.1',
    'yarl>=1.15.5',
    'zope.event>=5.0',
    'zope.interface>=7.0.3'
]

# Define optional dependencies in extras_require for specific use cases
extras_require = {
    'openai': ['openai>=1.53.0'],
    'anthropic': ['anthropic>=0.37.1', 'tokenizers>=0.20.1'], # Requires rust
    'ai': ['huggingface-hub>=0.25.2', 'tokenizers>=0.20.1', 'anthropic>=0.37.1'],
    'full': ['openai>=1.53.0', 'anthropic>=0.37.1', 'huggingface-hub>=0.25.2', 'tokenizers>=0.20.1']
}

# Main setup configuration
setup(
    name="fiscus",  # Package name as it will appear on PyPI or in package managers
    version="0.1.0a5",  # Version of the package (alpha release here)
    description="Fiscus is a powerful platform designed to be the API Gateway for the AI World.",
    long_description=long_description,  # Detailed description from README
    long_description_content_type="text/markdown",  # Content type for the long description
    author="Fiscus Flows, Inc.",  # Author or organization name
    author_email="support@fiscusflows.com",  # Contact email for support or inquiries
    url="https://github.com/fiscusflows/fiscus-sdk",  # Project URL (e.g., GitHub repository)
    license="Proprietary",  # License type (custom/proprietary here)
    
    # Finding and specifying package structure
    # packages=find_packages("src"),  # Discover packages within 'src' directory
    # package_dir={"": "src"},
    packages=['fiscus'],
	package_dir={"fiscus": "src/fiscus"},# Tell setuptools that packages are under 'src'
	package_data={"fiscus": ["*.so"]},
    # Cython extension modules configuration
    ext_modules=cythonize(
        extensions,
        compiler_directives={'language_level': "3"},  # Set Python language level for Cython
        annotate=False,  # Enable HTML annotations for debugging if True
    ),
    cmdclass={'build_ext': BuildExt},  # Use custom build_ext command to handle compilation errors

    # Setup-specific configurations
    zip_safe=False,  # Set to False if your package can't run from a zip archive
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    install_requires=install_requires,  # Core dependencies (required for all installations)
    extras_require=extras_require,  # Optional dependencies by feature

    # Metadata for package indexing
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.8",  # Minimum Python version required

    # Additional metadata for easier discovery on package repositories
    keywords="API Gateway AI Machine Learning",
)

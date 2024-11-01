from pathlib import Path
from setuptools import setup, find_packages

def get_requirements():
    """Get requirements while handling missing file case."""
    try:
        requirements = Path('requirements.txt').read_text().splitlines()
        return [r for r in requirements if r and not r.startswith('#')]
    except FileNotFoundError:
        print("Warning: requirements.txt not found")
        return []

def get_long_description():
    """Get README content while handling missing file and encoding cases."""
    try:
        # Try UTF-8 first (most common)
        return Path('README.md').read_text(encoding='utf-8')
    except FileNotFoundError:
        print("Warning: README.md not found")
        return ""
    except UnicodeDecodeError:
        try:
            # Fallback to system default encoding
            return Path('README.md').read_text()
        except Exception as e:
            print(f"Warning: Could not read README.md: {e}")
            return ""

setup(
    name='BertCC',
    version='0.1.0',
    install_requires=get_requirements(),
    packages=find_packages(),
    description='A context-aware Simplified to Traditional Chinese converter using BERT',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url='https://github.com/Benau/BertCC',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'bertcc = bertcc.__main__:main',
        ],
    },
    include_package_data=True
)

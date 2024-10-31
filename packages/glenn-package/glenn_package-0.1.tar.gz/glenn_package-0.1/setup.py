from setuptools import setup, find_packages

setup(
    name='glenn_package',  # Nama modul Anda
    version='0.1',      # Versi modul Anda
    packages=find_packages(),  # Temukan paket dalam folder
    install_requires=[],  # Daftar dependensi, jika ada
    author='Glenn Hakim',  # Nama Anda
    author_email='glenn.hkm@gmail.com',  # Email Anda
    description='Modul MK Glenn',
    long_description=open('README.md').read(),  # Deskripsi panjang dari README.md
    long_description_content_type='text/markdown',
    url='https://github.com/glennhkm/test-pypi.git',  # URL repositori
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Ubah sesuai lisensi Anda
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versi Python yang dibutuhkan
)

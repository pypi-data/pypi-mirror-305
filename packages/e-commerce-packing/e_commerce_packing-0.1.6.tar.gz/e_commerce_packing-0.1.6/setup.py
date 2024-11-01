# setup.py
from setuptools import setup, find_packages

setup(
    name="e-commerce-packing",
    version="0.1.6",  # Cập nhật phiên bản theo từng lần thay đổi
    packages=find_packages(),
    install_requires=[
        "requests",     # Để kiểm tra phiên bản mới nhất trên PyPI
        "mrjpacking",   # Thư viện cần cài đặt
    ],
    entry_points={
        "console_scripts": [
            "e-commerce-packing = e_commerce_packing.main:main",
        ],
    },
    author="Justin Nguyen",
    author_email="justinnguyen.7997@gmail.com",
    description="Gói hỗ trợ đóng hàng e-commerce",
    long_description="E-commerce-packing chương trình hỗ trợ đóng gói sản phẩm.",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

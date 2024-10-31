from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ntanh",  # tên của gói thư viện
    version="3.7.0",
    description="Thư viện hữu ích của Tuấn Anh.",
    url="https://pypi.org/project/ntanh/",
    author="Tuấn Anh - Foxconn",
    author_email="nt.anh.fai@gmail.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "ruamel.yaml",
        "pillow",
        "scikit-image",
        "lxml",
        "numpy",
        "tqdm",
    ],  # ultralytics 8.2.84 requires numpy<2.0.0,>=1.23.0  pip install numpy==1.26.4
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"ntanh": ["YOLO_Logic/*", "Thoi_gian/*", "ImageProcessing/*"]},
    # package_dir={"": "ntanh"},
    # packages=find_packages(where="ntanh"),
    Homepage="https://github.com/ntanhfai/tact",
    Issues="https://github.com/ntanhfai/tact/issues",
    entry_points={
        "console_scripts": [
            "ntanh=ntanh:console_main",
            "ntanh_aug=ntanh:console_image_aug",
            "ntanh_img_del=ntanh:console_fnImage_dupplicate_remove",
            "ntanh_base_params_help=ntanh:Print_BaseParam_using",
        ],
    },
)

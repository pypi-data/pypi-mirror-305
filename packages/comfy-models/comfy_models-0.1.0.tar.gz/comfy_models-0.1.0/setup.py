from setuptools import setup, find_packages

setup(
    name="comfy-models",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
        # add other dependencies
    ],
    entry_points={
        "console_scripts": [
            "models=comfy_models.cli:main",  # This makes your CLI command available
        ],
    },
    author="BennyKok",
    author_email="itechbenny@gmail.com",
    description="A collection of optimized ComfyUI-based cloud inference endpoints, built on [ComfyDeploy](https://github.com/BennyKok/comfyui-deploy) and [Modal](https://modal.com/).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/comfydeploy/models",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

import setuptools
 
with open("README.md", "r") as f:
    long_description = f.read()
 
setuptools.setup(
    name="busisfirstpackage",  # Replace with your package name
    version="1.0.0",  # Replace with your package version
    author="Busi Phathela",  # Replace with your name
    author_email="muvhusophathela@gmail.com",  # Replace with your email
    description="This is Busi's fiest package.",  # Brief package description
    long_description=long_description,
    long_description_content_type="text/markdown",
)

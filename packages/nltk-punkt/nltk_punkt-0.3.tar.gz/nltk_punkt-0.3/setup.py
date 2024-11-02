from setuptools import setup
from setuptools.command.install import install

# Download punkt during installation
def download_nltk_data():
    nltk.download('punkt_tab')

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        import nltk
        download_nltk_data()

setup(
    name="nltk_punkt",
    version="0.3",
    packages=["nltk_punkt"],
    # install_requires=[
    #     "nltk",
    # ],
    cmdclass={
        'install': PostInstallCommand,
    },
)

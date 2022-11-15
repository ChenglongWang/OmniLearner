#!bash

# Initial cleanup
rm -rf dist
rm -rf build
cd ../..
rm -rf dist
rm -rf build

# Creating a conda environment
conda create -n omnilearner_installer python=3.8 -y
conda activate omnilearner_installer

# Creating the wheel
python setup.py sdist bdist_wheel

# Setting up the local package
cd release/one_click_windows_gui
# Make sure you include the required extra packages and always use the stable or very-stable options!
pip install "../../dist/omnilearner-1.3-py3-none-any.whl"

# Creating the stand-alone pyinstaller folder
pip install pyinstaller==4.10
pyinstaller ../pyinstaller/omnilearner.spec -y
conda deactivate

# If needed, include additional source such as e.g.:
# cp ../../omnilearner/data/*.fasta dist/omnilearner/data

# Wrapping the pyinstaller folder in a .exe package
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" omnilearner_innoinstaller.iss
# WARNING: this assumes a static location for innosetup

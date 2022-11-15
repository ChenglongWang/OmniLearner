#!bash

# Initial cleanup
rm -rf dist
rm -rf build
FILE=OmicLearn.pkg
if test -f "$FILE"; then
  rm OmicLearn.pkg
fi
cd ../..
rm -rf dist
rm -rf build

# Creating a conda environment
conda create -n omnilearnerinstaller python=3.8 -y
conda activate omnilearnerinstaller

# Creating the wheel
python setup.py sdist bdist_wheel

# Setting up the local package
cd release/one_click_macos_gui
pip install "../../dist/omnilearner-1.3-py3-none-any.whl"

# Creating the stand-alone pyinstaller folder
pip install pyinstaller==4.10
pyinstaller ../pyinstaller/omnilearner.spec -y
conda deactivate

# If needed, include additional source such as e.g.:
# cp ../../omnilearner/data/*.fasta dist/omnilearner/data

# Wrapping the pyinstaller folder in a .pkg package
mkdir -p dist/omnilearner/Contents/Resources
cp ../logos/omnilearner_logo.icns dist/omnilearner/Contents/Resources
mv dist/omnilearner_gui dist/omnilearner/Contents/MacOS
cp Info.plist dist/omnilearner/Contents
cp omnilearner_terminal dist/omnilearner/Contents/MacOS
cp ../../LICENSE.txt Resources/LICENSE.txt
cp ../logos/omnilearner_logo.png Resources/omnilearner_logo.png
chmod 777 scripts/*

pkgbuild --root dist/omnilearner --identifier de.mpg.biochem.omnilearner.app --version 0.3.0 --install-location /Applications/OmicLearn.app --scripts scripts OmicLearn.pkg
productbuild --distribution distribution.xml --resources Resources --package-path OmicLearn.pkg dist/omnilearner_gui_installer_macos.pkg

PKG_NAME=mne-camcan-functional-connectivity-study
PYTHON_NAME=mne_camcan_func_connectivity_study
GH_NAME=massich

unameOut="$(uname -s)"

if [[ "${unameOut}" == "Linux" ]]; then
        git grep -l 'mne_camcan_func_connectivity_study' | xargs sed -i 's/mne_camcan_func_connectivity_study/'"${PYTHON_NAME}"'/g'
        git grep -l 'mne-camcan-functional-connectivity-study' | xargs sed -i 's/mne-camcan-functional-connectivity-study/'"${PKG_NAME}"'/g'
        sed -i 's/mne-tools/'"${GH_NAME}"'/g' README.rst
        sed -i 's/mne-project-template/'"${PKG_NAME}"'/g' README.rst
        sed -i 's/mne-tools/'"${GH_NAME}"'/g' setup.py
        sed -i 's/mne-project-template/'"${PKG_NAME}"'/g' setup.py
else
    git grep -l 'mne_camcan_func_connectivity_study' | xargs sed -i ' ' -e 's/mne_camcan_func_connectivity_study/'"${PYTHON_NAME}"'/g'
    git grep -l 'mne-camcan-functional-connectivity-study' | xargs sed -i ' ' -e 's/mne-camcan-functional-connectivity-study/'"${PKG_NAME}"'/g'
    sed -i ' ' -e 's/mne-tools/'"${GH_NAME}"'/g' README.rst
    sed -i ' ' -e 's/mne-project-template/'"${PKG_NAME}"'/g' README.rst
    sed -i ' ' -e 's/mne-tools/'"${GH_NAME}"'/g' setup.py
    sed -i ' ' -e 's/mne-project-template/'"${PKG_NAME}"'/g' setup.py
fi
mv mne_camcan_func_connectivity_study ${PYTHON_NAME}

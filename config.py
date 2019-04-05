import os.path as op

camcan_path = '/storage/store/data/camcan'
camcan_meg_path = op.join(
    camcan_path, 'camcan47/cc700/meg/pipeline/release004/')
camcan_meg_raw_path = op.join(camcan_meg_path, 'data/aamod_meg_get_fif_00001')

mne_camcan_freesurfer_path = (
    '/storage/store/data/camcan-mne/freesurfer')


derivative_path = '/storage/store/derivatives/camcan/pipelines/base2018/MEG'


import os
from os import uname

host = uname()[1]
user = os.environ['USER']

if host == 'toothless':
    subjects_dir = '/home/sik/Dropbox/Biomag2018_epilepsy_challenge/freesurfer'
    mne_data_path = '/home/sik/Dropbox/Biomag2018_epilepsy_challenge/original_data'
    # subjects_dir = '/home/sik/retreat/Biomag2018/freesurfer'
    # mne_data_path = '/home/sik/retreat/Biomag2018/original_data'
elif user == 'alex':
    subjects_dir = '/Users/alex/Dropbox/Biomag2018_epilepsy_challenge/freesurfer'
    mne_data_path = '/Users/alex/Dropbox/Biomag2018_epilepsy_challenge/original_data'
    # subjects_dir = '/Users/alex/work/data/retreat_project1/Biomag2018/freesurfer'
    # mne_data_path = '/Users/alex/work/data/retreat_project1/Biomag2018/original_data'
elif user == 'hichamjanati':
    subjects_dir = '/Users/hichamjanati/Dropbox/Biomag2018_epilepsy_challenge/freesurfer'
    mne_data_path = '/Users/hichamjanati/Dropbox/Biomag2018_epilepsy_challenge/original_data'
else:
    subjects_dir = '/storage/store/data/biomag_challenge/Biomag2018/freesurfer'
    mne_data_path = '/storage/store/data/biomag_challenge/Biomag2018/original_data'

subject_ids = ('226', '245', '251')

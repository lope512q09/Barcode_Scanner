@ECHO OFF

call <anaconda_dir>/Scripts/activate.bat <anaconda_dir>

python data_transfer.py

PAUSE
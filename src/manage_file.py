import os
from os import listdir
from os.path import isfile, join


def ensure_dir(file_path):
	directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
			os.makedirs(directory)

def list_files(dir_path):
	files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
	return files
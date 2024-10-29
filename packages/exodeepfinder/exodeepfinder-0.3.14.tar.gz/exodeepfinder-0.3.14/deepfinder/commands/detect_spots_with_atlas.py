from deepfinder.commands import utils
utils.run_with_python_on_windows(__file__)
import os
import shutil
from pathlib import Path
import subprocess
from deepfinder.commands.convert_tiff_to_h5 import convert_tiff_to_h5, get_tiff_files

def get_full_path_if_defined(parent, filename):
	return str(parent / filename) if parent is not None else filename

def detect_spots(tiffs_path, atlas_path, atlas_args, output_path):
	output_path = Path(str(output_path).replace('{movie.name}', tiffs_path.name).replace('{movie.parent}', str(tiffs_path.parent)))
	output_folder = output_path.with_suffix('')
	output_folder.mkdir(exist_ok=True, parents=True)

	# Make paths absolute since cwd will change
	atlas_path = Path(atlas_path).resolve() if atlas_path is not None else None
	tiffs_path = Path(tiffs_path).resolve()
	output_folder = Path(output_folder).resolve()
	output_path = Path(output_path).resolve()

	parent = Path('.atlas')
	parent.mkdir(exist_ok=True)
	cwd = os.getcwd()
	os.chdir(parent)
	blobs = Path('blobs.txt')
	if not blobs.exists():
		print('Generating blobs.txt...')
		subprocess.run([get_full_path_if_defined(atlas_path, 'blobsref')])

	for frame in sorted(list(tiffs_path.iterdir())):
		if frame.suffix.lower() == '.tif' or frame.suffix.lower() == '.tiff':
			print(f'Processing {frame}...')
			subprocess.run([get_full_path_if_defined(atlas_path, 'atlas'), '-i', str(frame), '-o', str(output_folder / frame.name)] + atlas_args.split(' '))

	if not output_folder.exists():
		raise Exception(f'An error occured during  detections. The output folder {output_folder} does not exist.')
	
	frames = get_tiff_files(output_folder)

	if len(frames)==0:
		raise Exception(f'An error occured during the bright spot detections. The output folder path {output_folder} does not contain any tiff file (no frames).')

	print('Convert detection frames to h5 format...')

	try:
		convert_tiff_to_h5(output_folder, output_path, make_subfolder=False)
	except Exception as e:
		print(f'An exception occured during the conversion of the output detections (in {output_folder}). It is likely that a problem which occured during the detections causes this exception.')
		raise e
	
	shutil.rmtree(output_folder)

	os.chdir(cwd)
	return

utils.ignore_gooey_if_args()

def create_parser(parser=None, command=Path(__file__).stem, prog='Detect spots', description='Detect spots and convert resulting segmentation to h5.'):
	return utils.create_parser(parser, command, prog, description)

def add_args(parser):
	parser.add_argument('-m', '--movie', help='Path to the input folder containing one tiff file per frame.', default='tiff/', type=Path, widget='DirChooser')
	parser.add_argument('-ap', '--atlas_path', help='Optional path to atlas (None by default since atlas is supposed to be installed with conda thus directly accessible).', default=None, type=Path)
	parser.add_argument('-aa', '--atlas_args', help='Additional atlas arguments.', default='-rad 21 -pval 0.001 -arealim 3', type=str)
	parser.add_argument('-o', '--output', help='Path to the output segmentations. If used, the {movie.name} string will be replaced by the --movie file name, and {movie.parent} by the movie parent folder.', default='{movie.parent}/detector_segmentation.h5', type=Path, widget='FileSaver')
	parser.add_argument('-b', '--batch', help='Path to the root folder containing all folders to process. If given, the --movie argument must be relative to the folder to process.', default=None, type=Path, widget='DirChooser')

@utils.Gooey
def main(args=None):

	args = utils.parse_args(args, create_parser, add_args)

	movie_paths = sorted([d for d in args.batch.iterdir() if d.is_dir()]) if args.batch is not None else [args.movie]

	for movie_path in movie_paths:
		print('Process', movie_path)
		tiff_path = movie_path / args.movie if args.batch is not None else args.movie
		detect_spots(tiff_path, args.atlas_path, args.atlas_args, args.output)

if __name__ == '__main__':
	main()
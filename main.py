import src.image_processing as ip
import src.manage_file as mf

def score_images(base_path):
	files = mf.list_files(base_path)
	scores = [
		(
			ip.detect_blur_fft(ip.gray_image(base_path+file), 50, 10, file.split(".")[0]), 
			file
		) for file in files]
	
	return scores

def main():
	scores = score_images("images/")
	print(scores)
	pass

main()
import src.image_processing as ip
import src.manage_file as mf

def score_images(base_path):
	files = mf.list_files(base_path)
	scores = [
		(
			ip.detect_blur_fft(ip.gray_image(base_path+file), 60, file.split(".")[0]), 
			file
		) for file in files]
	
	return scores

def main():
	scores = score_images("images/")
	sorted_scores = sorted(scores, key=lambda a: a[0], reverse=True)

	print(sorted_scores)
	pass

main()
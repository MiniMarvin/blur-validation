import src.image_processing as ip
import src.manage_file as mf

def score_images(base_path, filter_type="square"):
	files = mf.list_files(base_path)
	scores = [
		(
			ip.detect_blur_fft(ip.gray_image(base_path+file), 60, filter_type, file.split(".")[0]), 
			file
		) for file in files]
	
	return scores

def main():
	scores = score_images("images/", "smooth_square")
	sorted_scores = sorted(scores, key=lambda a: a[0], reverse=True)

	print(sorted_scores)
	pass

main()
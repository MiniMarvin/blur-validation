import src.image_processing as ip
import src.manage_file as mf

def score_images(base_path, filter_type="square", ranking_type="mean"):
	files = mf.list_files(base_path)
	scores = [
		(
			ip.detect_blur_fft(ip.gray_image(base_path+file), 60, filter_type, ranking_type, file.split(".")[0] + "_" + filter_type), 
			file
		) for file in files]
	
	return scores
    
def main():
  scores = score_images("images/")
  sorted_scores = sorted(scores, key=lambda a: a[0], reverse=True)

  for score in sorted_scores:
    s = score[1] + "\t|\t" + str(score[0])
    print(s)
  print()

main()
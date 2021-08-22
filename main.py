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

def compare_scores():
  for tp in ["square", "smooth_square", "circle", "smooth_circle"]:
    scores = score_images("images/", tp)
    sorted_scores = sorted(scores, key=lambda a: a[0], reverse=True)
    print(tp)
    for score in sorted_scores:
      s = score[1] + "\t|\t" + str(score[0])
      print(s)
    print()
    

def main():
	# scores = score_images("images/", "smooth_square")
	# sorted_scores = sorted(scores, key=lambda a: a[0], reverse=True)

	# print(sorted_scores)
  compare_scores()
  pass

main()
import os 

def rmQ(fname):
	return fname.split("?")[0]
	
def getImageURL(src, url):
	if "http" not in src:
		return url + src
		
	else:
		return src
		
def mkdir(dirName):
	try:
		
		path = '/home/munemura/virtualenvs/cv/lib/python3.4/sitepackges/my_project/data/'
		Abspath = os.path.abspath(path)
		print("絶対パスは", Abspath, "である。")
		
		os.mkdir(dirName)
	
	except Eception as e:
		print e
		
#   pass # if dirName already exist

def DLImages(AllImages):
	import urllib
	
	successNum = 0
	for img in AllImages:
		src = img.get("src")
		imgURL = getImageURL(src, url)
		fname = src.split("/")[-1]
		
		if "?" in fname:
			fname = rmQ(fname)
		try:
			if fname in os.listdir(dirName):
				fname = fname + src(successNum)
			urllib.urlretrieve(imgURL, dirName+"/"+fname)
			print ("[Success]" + imgURL)
			successNum += 1
			
		except Exception as e:
			print e
			print ("[Failed]" + imgURL)
			return successNum
			
def main():
	from bs4 import BeautifulSoup
	from urllib import request
	
	mkdir(dirName)
	response = request.urlopen("http://www.cdtdb.neuroinf.jp/CDT/") #BrainTXのURL
	html = response.read()
	soup = BeautifulSoup(html)
	AllImages = soup.find_all("img")
	imgNum = len(AllImages)
	successNum = DLImages(AllImages, url, dirName)
	
	print successNum, "images could be downloaded (in", imgNum, "images.)"
	
if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		main(sys. argv[1])
	elif len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
 
		
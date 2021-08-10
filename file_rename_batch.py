import os 

def rename(path,word_remove):
	for x in os.listdir(path):
		if word_remove in x:
			file_path = os.path.join(path, x)
			new_path = os.path.join(path, x.replace(word_remove, ''))
			print(f'Files Renamed \n \n {os.path.basename(new_path)} \n \n')
			os.renames(file_path, new_path)
			


path = input('Enter path here : ') 
word_remove = input('Enter the word to remove : ')

rename(path,word_remove)
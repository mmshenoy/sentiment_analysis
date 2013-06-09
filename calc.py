import sys
import os

class Word:
	
	def __init__(self):
		self.val = 0
		self.instances = 0
		
	def getVal(self):
		return int(self.val)
	
	def getInst(self):
		return self.instances
	
	def setWord(self,val,instances):
		self.val = val
		self.instances = instances
	
def main():
    dir_name = 'D:\\Code\\GitHub\\sentiment\\song_files'
    corpus_file = open(sys.argv[1])
    scores = {}
    song_score = 0
    song_words = 0
	
    for line in corpus_file:
		term, score = line.split("\t")
		word_obj = Word()
		word_obj.setWord(score,-1)
		scores[term] = word_obj

    write_file = open('output.csv','wb')
	
    for files in os.listdir(dir_name):
		print files
		song_file = open(dir_name + '\\' + files)
		for line in song_file:
			if len(line) > 0:
				#print line
				words = line.split()
				line_score = 0
				line_words = len(words)
				for word in words:
					#print word
					if scores.has_key(word):
						#print scores[word].getVal()
						line_score += scores[word].getVal()
				#print 'Line Avg: ' + str(float(line_score)/line_words)
				song_score += line_score
				song_words += line_words
		
		song_avg = float(song_score)/song_words
		print 'Song Score: ' + str(song_score) + '\nSong Avg: ' + str(song_avg)
		objs = files.split('_')
		band = objs[0]
		year = objs[1]
		song = objs[2].split('.')[0]
		row = band + ',' + song + ',' + year + ',' + str(song_score) + ',' + str(song_avg)
		write_file.write(row)
		
    write_file.close()
	
if __name__ == '__main__':
    main()

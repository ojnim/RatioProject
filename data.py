from RatioProject.processing import txt_to_csv, word_filter

#languages
languages = ['ko','en']

#file path of the first language
file1 = './korean-parallel-corpora/korean-english-news-v1/korean-english-park.train/korean-english-park.train.ko'
#file path of the second language
file2 = './korean-parallel-corpora/korean-english-news-v1/korean-english-park.train/korean-english-park.train.en'

#source name
source = 'news_train'

word = 'per'

csv_file = txt_to_csv(source,file1, file2, languages)

word_filter(csv_file, source, word)
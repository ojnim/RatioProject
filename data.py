from RatioProject.processing import txt_to_csv, word_filter

#languages
languages = ['en','ko']

#file path
ko_file = './korean-parallel-corpora/korean-english-news-v1/korean-english-park.train/korean-english-park.train.ko'
en_file = './korean-parallel-corpora/korean-english-news-v1/korean-english-park.train/korean-english-park.train.en'

#source name
source = 'news_train'

word = 'per'


csv_file = txt_to_csv(source,ko_file, en_file, languages)

word_filter(csv_file, source, word)
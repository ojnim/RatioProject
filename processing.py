import pandas as pd

def txt_to_csv(source, file1, file2, languages):
    #read txt file
    with open(file1, 'r', encoding='utf-8') as f:
        f1_lines = f.readlines()
    
    with open(file2, 'r', encoding='utf-8') as f:
        f2_lines = f.readlines()

    df = pd.DataFrame({
        source: range(1, len(f1_lines) + 1), #row number
        languages[0]: [line.strip() for line in f1_lines],
        languages[1]: [line.strip() for line in f2_lines]
    })

    csv_file = f'{source}.csv'
    df.to_csv(csv_file, index=False)

    return csv_file

def word_filter(csv_file, source, word):
    df = pd.read_csv(csv_file, header=0)
    spaced_word = ' ' + word + ' '

    filtered_df = df[df["en"].str.contains(spaced_word)]
    filtered_csv_file = f'{word}_{source}.csv'
    filtered_df.to_csv(filtered_csv_file, index=False)

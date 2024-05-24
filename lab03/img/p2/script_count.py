def count_words(input_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        words = infile.readlines()
    
    total_words = len(words)
    
    print(f"Total words in {input_file}: {total_words}")

if __name__ == "__main__":
    input_file1 = 'rockyou.txt'
    input_file2 = 'rockyou_mod.dic'
    count_words(input_file1)
    count_words(input_file2)



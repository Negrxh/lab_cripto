def process_wordlist(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
        words = infile.readlines()
    
    modified_words = []
    
    for word in words:
        word = word.strip()  # Remove any leading/trailing whitespace/newlines
        if not word or word[0].isdigit():
            continue
        modified_word = word.capitalize() + '0'
        modified_words.append(modified_word)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for word in modified_words:
            outfile.write(word + '\n')

if __name__ == "__main__":
    input_file = 'rockyou.txt'
    output_file = 'rockyou_mod.dic'
    process_wordlist(input_file, output_file)
    print(f"Processed words have been written to {output_file}")



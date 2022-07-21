class Piglatin:
    trials = int(input("Enter the number of times you want to run this program"))

    def piglatin(self):
        pig_latin = ""
        while self.trials > 0:
            word = input("Type in the word you want to convert to pig latin (no spaces)")
            char_1_list = word[:1]
            for i in range(1):
                if char_1_list == "a".lower() or char_1_list == "e".lower() or char_1_list == \
                        "i".lower() or char_1_list == "o".lower() or char_1_list == "u".lower():
                    pig_latin += word + "way"
                    print(pig_latin)
                else:
                    new_word_list = word.split(char_1_list)
                    new_word = ''.join(new_word_list)
                    char_1 = ''.join(char_1_list)
                    pig_latin += new_word + char_1 + "ay"
                    print(pig_latin)
                self.trials -= 1
            self.piglatin()


pig = Piglatin()
pig.piglatin()

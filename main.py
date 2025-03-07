# Generator text based on input with Markov Chain
import random
class MarkovChain:
    def __init__(self):
        self.chain = {} # constructor for init dictionary

    def training(self, text):
        words = text.split()

        for i in range(len(words) - 1):
            word = words[i]
            nextWord = words[i+1]

            if word not in self.chain:
                self.chain[word] = []
            self.chain[word].append(nextWord)

    def generation(self, length=10):
        if not self.chain:
            print("Chain is not trainer yet! wtf")

        word = random.choice(list(self.chain.keys()))
        resultArr = [word]

        for _ in range(length - 1):
            nextWords = self.chain.get(word, [])
            if not nextWords:
                break
            word = random.choice(nextWords)
            resultArr.append(word)

        return " ".join(resultArr)

text = "сонце світить я гуляю парк гарний я люблю природу"
gen = MarkovChain()
gen.training(text)

print(f"Input text: {text} \n")

for i in range(5):
    generatedText = gen.generation(10)
    print(f"Generated {i + 1}: {generatedText}")

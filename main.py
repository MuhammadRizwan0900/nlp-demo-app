from tokenization import tokenize_text


sentences, words = tokenize_text()
tokenizationOutput = open('tokenization-output.txt', 'w+')
tokenizationOutput.write("Sentences output:")
tokenizationOutput.write(str(sentences))
tokenizationOutput.write("\n")
tokenizationOutput.write("Words output:")
tokenizationOutput.write(str(words))
print("Sentences: ", sentences)
print("Words: ", words)


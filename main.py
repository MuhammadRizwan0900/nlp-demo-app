from tokenization import tokenize_text

tokenize_text()
# tokenizationOutput = open('tokenization-output.txt', 'w+')
# tokenizationOutput.write("Sentences output:")
# tokenizationOutput.write(str(sentences))
# tokenizationOutput.write("\n")
# tokenizationOutput.write("Words output:")
# tokenizationOutput.write(str(words))
# print("Sentences: ", sentences)
# print("Words: ", words)
#Perform these steps
#Tokenize the text into sentences.
#Tokenize each sentence into words.
#Convert all the text to lowercase.
#Remove all punctuation marks and special characters.
#Remove stop words (such as "the," "a," "an," "and," etc.) to reduce noise in the data.
#Perform stemming or lemmatization to reduce words to their root form
# import openai
# openai.api_key = "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"
#
# response = openai.Completion.create(
#     model="curie:ft-personal-2023-04-10-07-04-48",
#     prompt="shipping")
# print('resp:::', response.choices[0].text)

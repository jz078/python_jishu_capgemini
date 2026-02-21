# extract all words starting with a vowel from a sentence.

s = "Hello, my name is Jishu Mahato. I am from Hura, Purulia."

words = s.split()

vowel_words = [w for w in words if w[0].lower() in "aeiou"]

print(vowel_words)
import nltk
import sys
import os


def main():
    # Read data from file
    if len(sys.argv) != 2:
        sys.exit("Usage: python sentiment.py corpus")
    positives, negatives = load_data(sys.argv[1])

    # Create a set of all words 
    words = set()
    for document in positives:
        words.update(document)
    for document in negatives:
        words.update(document)

    # Extract fearure from text
    training = []
    training.extend(generate_features(positives, words, "Positive"))
    training.extend(generate_features(negatives, words, "Negative"))

    # Clasify a new sample 
    classifier = nltk.NaiveBayesClassifier.train(training)
    sentence = input("Sentence: ")
    result = (classify(classifier, sentence, words))
    for key in result.samples():
        print(f"{key}: {result.prob(key):.4f}")

# Load positive and negative documents from the corpus directory
def load_data(corpus):
    positives = []
    negatives = []
    positives_path = os.path.join(corpus, "positives.txt")
    negatives_path = os.path.join(corpus, "negatives.txt")

    # Read positive sentences
    with open(positives_path, encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line:
                tokens = nltk.word_tokenize(line)
                positives.append(tokens)

    # Read negative sentences
    with open(negatives_path, encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line:
                tokens = nltk.word_tokenize(line)
                negatives.append(tokens)

    return positives, negatives

# Generate features for each document
def generate_features(emotion, words, label):
    features = []
    for document in emotion:
        doc_words = set(document)
        feats = {}

        for word in words:
            feats[f"contains({word.lower()})"] = (word.lower() in [w.lower() for w in doc_words])

        features.append((feats, label))

    return features

# Classify a sentence and return the probability distribution
def classify(classifier, sentence, words):
    tokens = nltk.word_tokenize(sentence)
    feats = {}
    tokens_lower = [w.lower() for w in tokens]

    for word in words:
        feats[f"contains({word.lower()})"] = (word.lower() in tokens_lower)
        
    return classifier.prob_classify(feats)


if __name__ == "__main__":
    main()
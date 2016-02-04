from argparse import ArgumentParser
from classify import *

parser = ArgumentParser(description="Naive Bayes Spam Filter")
parser.add_argument("spam_examples", help="spam example messages folder")
parser.add_argument("ham_examples", help="ham example messages folder")
parser.add_argument("spam_test", help="test messages folder")
parser.add_argument("ham_test", help="test messages folder")
parser.add_argument("-init_prob_spam", help="initial probability of a message being spam (0-1)", default="0.5", type=float)
parser.add_argument("-occurence_threshold", help="number of times a word must appear in spam and ham messages overall", default="10", type=int)
parser.add_argument("-score_threshold", help="spam score above which a message must be rated to be considered spam (0-1)", default="0.9", type=float)
parser.add_argument("-phrase_length", help="maximum length of word phrases considered (higher phrase lengths will impact performance)", default="1", type=int)
args = parser.parse_args()

# Get initial probability of spam
init_prob_spam = args.init_prob_spam

# Get thresholds
occurence_threshold = args.occurence_threshold
score_threshold = args.score_threshold

# Get messages from files
spam_example_messages = get_messages(args.spam_examples)
ham_example_messages = get_messages(args.ham_examples)
spam_test_messages = get_messages(args.spam_test)
ham_test_messages = get_messages(args.ham_test)

# Get spam and ham word occurences per message
spam_words = get_word_occurences(spam_example_messages, args.phrase_length)
ham_words = get_word_occurences(ham_example_messages, args.phrase_length)
spam_test_words = get_word_occurences(spam_test_messages, args.phrase_length)
ham_test_words = get_word_occurences(ham_test_messages, args.phrase_length)

# Get overall spam and ham word frequencies
spam_word_frequencies = get_word_frequencies(spam_words)
ham_word_frequencies = get_word_frequencies(ham_words)

# Get word spamicities
word_spamicities = get_word_spamicities(spam_word_frequencies, ham_word_frequencies, init_prob_spam, occurence_threshold)

# Successful classifications count
spam_successes = 0
ham_successes = 0

# Classify test emails as spam or ham
for key in sorted(spam_test_words):
    message_score = get_spam_score(spam_test_words[key], word_spamicities)
    # print(key, ":", message_score)
    if message_score > score_threshold:
        spam_successes += 1

for key in sorted(ham_test_words):
    message_score = get_spam_score(ham_test_words[key], word_spamicities)
    # print(key, ":", message_score)
    if message_score < score_threshold:
        ham_successes += 1

# Calculate and display success rates
spam_success_rate = spam_successes / len(spam_test_messages)
ham_success_rate = ham_successes / len(ham_test_messages)

# Output results
print("Spam success rate: {0:.2f}%".format(spam_success_rate * 100))
print("Ham success rate: {0:.2f}%".format(ham_success_rate * 100))

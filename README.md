# Spam Classifier

This is a spam classifier that uses naive Bayesian probability. I created it as
a proof of concept spam filter for a college course.

The classifier first takes a body of known spam and ham (non-spam) emails to
evaluate. Then, it evaluates each email in a test body of emails as spam or ham,
with the difference between ham and spam only known to the classifier for the
purpose of calculating the success rate.

Several parameters can be changed to optimize the effectiveness of the
classifier. By tweaking these parameters, rates in the upper 90% range for both
spam and ham classification can be reached.

Included is a sample of Apache SpamAssassin’s public corpus of spam and ham
emails for testing. I've also included the paper I wrote and the presentation I
created for the project. These both detail the implementation details of the
naive Bayesian probabilistic approach to spam filtering and its effectiveness.


Usage is documented in the help output from `python spam_classifier.py -h`:

    usage: spam_classifier.py [-h] [-init_prob_spam INIT_PROB_SPAM]
                              [-occurence_threshold OCCURENCE_THRESHOLD]
                              [-score_threshold SCORE_THRESHOLD]
                              [-phrase_length PHRASE_LENGTH]
                              spam_examples ham_examples spam_test ham_test

    Naive Bayes Spam Filter

    positional arguments:
      spam_examples         spam example messages folder
      ham_examples          ham example messages folder
      spam_test             test messages folder
      ham_test              test messages folder

    optional arguments:
      -h, --help            show this help message and exit
      -init_prob_spam INIT_PROB_SPAM
                            initial probability of a message being spam (0-1)
      -occurence_threshold OCCURENCE_THRESHOLD
                            number of times a word must appear in spam and ham
                            messages overall
      -score_threshold SCORE_THRESHOLD
                            spam score above which a message must be rated to be
                            considered spam (0-1)
      -phrase_length PHRASE_LENGTH
                            maximum length of word phrases considered (higher
                            phrase lengths will impact performance)


## Example

As an example, this is what the tweaked input values for the supplied test data
look like:

    python spam_classifier.py spam_examples ham_examples spam_test ham_test
           -init_prob_spam 0.7 -occurence_threshold 5 -phrase_length 5


After evaluating the contents of the emails (which can take a few seconds given
that a phrase length of 5 was used), the classification success rates are
displayed:

    Spam success rate: 98.00%
    Ham success rate: 99.50%

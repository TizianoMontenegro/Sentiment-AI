# Sentiment AI - Sentiment Analysis Tool

![Sentiment Analysis](https://img.shields.io/badge/Python-3.8%2B-blue) ![NLTK](https://img.shields.io/badge/NLTK-3.7-yellowgreen) ![License](https://img.shields.io/badge/License-MIT-green)

Sentiment AI is a Python-based sentiment analysis tool that uses natural language processing to determine the emotional tone of text input. Powered by NLTK's Naive Bayes classifier, this tool can predict whether a given sentence expresses positive or negative sentiment with probability scores.

## Key Features

- 🧠 **Machine Learning Classifier**: Utilizes NLTK's Naive Bayes algorithm for sentiment classification
- 📊 **Probability Scores**: Provides detailed probability distribution for sentiment classes
- 📁 **Customizable Corpus**: Easily expandable with your own positive/negative text samples
- 🔧 **Simple Interface**: Clean command-line interface for quick analysis
- 🐍 **Python Implementation**: Lightweight and easy to integrate with other Python projects

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TizianoMontenegro/Sentiment-AI.git
cd Sentiment-AI
```

2. Install required dependencies:
```bash
pip install nltk
```

3. Download NLTK data resources:
```python
python -c "import nltk; nltk.download('punkt')"
```

## Usage

Run the sentiment analysis tool with the included corpus:
```bash
python sentiment.py corpus
```

Example interaction:
```
Sentence: I'm feeling wonderful today!
Positive: 0.8732
Negative: 0.1268
```

## Corpus Structure

The tool uses two text files for training:

- `corpus/positives.txt`: Contains positive sentiment sentences
- `corpus/negatives.txt`: Contains negative sentiment sentences

You can customize these files with your own data to improve the classifier's accuracy for specific domains.

### Adding New Training Data
1. Open the respective text file
2. Add new sentences (one per line)
3. Save the file
4. Rerun the classifier

## Dependencies

- Python 3.8+
- [NLTK](https://www.nltk.org/) (Natural Language Toolkit)
- NLTK Data (punkt tokenizer models)

## Contributing

Contributions are welcome! To contribute to Sentiment AI:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

Please ensure your code follows PEP 8 style guidelines and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [[LICENSE](LICENSE)] file for details.

## Acknowledgments

- Natural Language Toolkit ([NLTK](https://www.nltk.org/)) team
- All contributors who help improve this project

---

**Note**: This is an educational project. For production sentiment analysis, consider using more advanced models like BERT or commercial NLP APIs.

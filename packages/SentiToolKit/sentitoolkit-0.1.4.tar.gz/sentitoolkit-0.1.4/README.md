
# SentiToolKit &nbsp; ![version](https://img.shields.io/badge/version-0.1.4-blue) ![Python](https://img.shields.io/badge/python-3.6%2B-brightgreen) ![License](https://img.shields.io/badge/license-GNU%20License-yellow)

SentiToolKit is a simple sentiment analysis library that leverages LSTM (Long Short-Term Memory) neural networks for predicting the sentiment of a given text. This toolkit provides a streamlined interface for text preprocessing, model loading, and prediction.

## ✨ Features

- **Pre-trained Model**: Uses a trained LSTM model for sentiment analysis.
- **Tokenization Support**: Handles text tokenization with a customizable vocabulary size.
- **Sentiment Prediction**: Predicts whether a text is `Positive`, `Neutral`, or `Negative`.
- **Easy to Use**: Minimal setup required to get predictions.
- **Customizable**: You can use your own tokenizer and model for fine-tuning.

## 📦 Installation

You can install the `SentiToolKit` package via pip:

```bash
pip install SentiToolKit
```

Alternatively, if you'd like to build from source:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/SentiToolKit.git
    ```

2. Navigate to the project directory and install the package:

    ```bash
    cd SentiToolKit
    pip install .
    ```

## 🚀 Quickstart

To get started with SentiToolKit, follow the example below:

```python
from SentiToolKit import SentiToolKit

# Initialize the sentiment toolkit with pre-trained model and tokenizer
senti_toolkit = SentiToolKit(model_path='SentiToolKit.keras', tokenizer_path='tokenizer.pkl')

# Predict the sentiment of a sentence
result = senti_toolkit("I love using SentiToolKit for sentiment analysis!")
print(f"Predicted sentiment: {result}")  # Output: Positive
```

## 🧰 Usage

1. **Loading the Pre-trained Model**: The toolkit loads a pre-trained LSTM model from the provided `.keras` file.
2. **Text Tokenization**: The input text is tokenized and padded using the stored tokenizer from `tokenizer.pkl`.
3. **Sentiment Prediction**: Predicts the sentiment based on the input text:
   - `Positive`
   - `Neutral`
   - `Negative`

## 📁 Project Structure

```
SentiToolKit/
├── SentiToolKit/
│   ├── __init__.py
│   ├── toolkit.py
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── tokenizer.pkl
├── SentiToolKit.keras
```

## 📄 License

This project is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE Version 3,. See the [LICENSE](LICENSE) file for details.

## 💡 Future Improvements

- Add support for additional languages.
- Fine-tune the pre-trained model for domain-specific tasks.
- Implement an API for real-time sentiment analysis.

## 👥 Contributing

Contributions are welcome! If you’d like to contribute to SentiToolKit, feel free to fork the repository and submit a pull request.

1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## 📬 Contact

- Author: [Niall Dcunha](mailto:dcunhaniall@gmail.com)
- GitHub: [https://github.com/Niall1985](https://github.com/Niall1985)

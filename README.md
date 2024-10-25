# Semantic Router

**Semantic Router** is a conversational routing system designed to help chatbots navigate different conversation topics or intents based on semantic similarity. This allows bots to selectively respond to specific topics, such as steering clear of political discussions or switching to a friendly "chitchat" mode based on user input. The router uses natural language encoders (from Cohere or OpenAI) to classify input messages into predefined routes.

## Features

- Routes specific user inputs into designated conversation topics using semantic similarity.
- Helps conversational agents handle specific types of interactions, such as avoiding certain subjects (e.g., politics) or transitioning to a casual conversation style.
- Supports multiple encoding backends, including Cohere and OpenAI.

## Prerequisites

- **Python 3.8** or higher
- **API Keys**:
  - **Cohere API Key** (for `CohereEncoder`)
  - **OpenAI API Key** (for `OpenAIEncoder`)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Semantic-Router.git
   cd Semantic-Router
   ```

2. **Install Dependencies**:
   Install the dependencies with `pip`:
   ```bash
   pip install -r requirements.txt
   ```
   
   Ensure `semantic_router` and its dependencies are included in `requirements.txt`. Otherwise, install it directly:
   ```bash
   pip install semantic_router
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root to store API keys:
   ```env
   COHERE_API_KEY=your_cohere_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```
   
   Replace `your_cohere_api_key` and `your_openai_api_key` with your actual API keys.

## Usage

The following example demonstrates how to set up routing based on semantic similarity, classify inputs, and identify topics (e.g., `politics`, `chitchat`). The `main.py` file contains the core usage.

### Defining Routes

Define specific conversation routes by initializing `Route` objects with a `name` and a list of `utterances` that represent sample phrases or topics for classification.

```python
from semantic_router import Route

# Define routes for specific conversational topics
politics = Route(
    name="politics",
    utterances=[
        "isn't politics the best thing ever",
        "why don't you tell me about your political opinions",
        "don't you just love the president",
        "they're going to destroy this country!",
    ],
)

chitchat = Route(
    name="chitchat",
    utterances=[
        "how's the weather today?",
        "how are things going?",
        "lovely weather today",
        "let's go to the chippy",
    ],
)
```

### Initializing the Encoder and Route Layer

Set up an encoder (either `CohereEncoder` or `OpenAIEncoder`) based on your preference. Then initialize the `RouteLayer`, which manages the routes and handles classification.

```python
from semantic_router.encoders import CohereEncoder, OpenAIEncoder
from semantic_router.layer import RouteLayer
import os

# Choose the encoder and set up API keys
os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")
encoder = CohereEncoder()  # or OpenAIEncoder() for OpenAI

# Add routes to the layer
routes = [politics, chitchat]
rl = RouteLayer(encoder=encoder, routes=routes)
```

### Classifying User Input

Use the `RouteLayer` instance to classify incoming messages. The system will return the name of the matched route or `None` if no suitable route is found.

```python
print(rl("don't you love politics?").name)        # Outputs: "politics"
print(rl("how's the weather today?").name)        # Outputs: "chitchat"
print(rl("I'm interested in learning about llama 2").name)  # Outputs: None
```

## Examples

To test the routing in your terminal, run:

```bash
python main.py
```

Expected Output:
```plaintext
RouteChoice(name='politics', function_call=None, similarity_score=None)
RouteChoice(name='chitchat', function_call=None, similarity_score=None)
RouteChoice(name=None, function_call=None, similarity_score=None)
```

## Contributing

If you’d like to contribute, please fork the repository and submit a pull request. Suggestions and improvements are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Cohere](https://cohere.ai) and [OpenAI](https://openai.com) for their natural language processing APIs.

from semantic_router import Route
from semantic_router.encoders import CohereEncoder, OpenAIEncoder
from semantic_router.layer import RouteLayer

import os


# we could use this as a guide for our chatbot to avoid political conversations
politics = Route(
    name="politics",
    utterances=[
        "isn't politics the best thing ever",
        "why don't you tell me about your political opinions",
        "don't you just love the president" "don't you just hate the president",
        "they're going to destroy this country!",
        "they will save the country!",
    ],
)

# this could be used as an indicator to our chatbot to switch to a more
# conversational prompt
chitchat = Route(
    name="chitchat",
    utterances=[
        "how's the weather today?",
        "how are things going?",
        "lovely weather today",
        "the weather is horrendous",
        "let's go to the chippy",
    ],
)


# for Cohere
os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")
encoder = CohereEncoder()

# or for OpenAI
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
encoder = OpenAIEncoder()

# we place both of our decisions together into single list
routes = [politics, chitchat]


rl = RouteLayer(encoder=encoder, routes=routes)

print(rl("don't you love politics?").name)
# prints out "RouteChoice(name='politics', function_call=None, similarity_score=None)"

print(rl("how's the weather today?").name)
# prints out "RouteChoice(name='chitchat', function_call=None, similarity_score=None)"

print(rl("I'm interested in learning about llama 2").name)
# prints out "RouteChoice(name=None, function_call=None, similarity_score=None)"
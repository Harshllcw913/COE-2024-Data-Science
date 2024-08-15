from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Replace with your own key and endpoint
key = "YOUR_API_KEY"
endpoint = "YOUR_ENDPOINT_URL"


# Authenticate the client
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credential=ta_credential
    )
    return text_analytics_client


client = authenticate_client()


# Analyze sentiment of movie reviews
def sentiment_analysis_example(client):

    # Sample movie reviews
    reviews = [
        "The movie was fantastic! I loved the story and the acting was great.",
        "I did not like this movie at all. It was too slow and boring.",
        "It was an average movie. Some parts were good, but others were not so much.",
        "Great movie! Would definitely watch again.",
        "Terrible movie. Waste of time.",
    ]

    response = client.analyze_sentiment(documents=reviews)
    for idx, doc in enumerate(response):
        print(f"Review {idx + 1}:")
        print(f"Document Sentiment: {doc.sentiment}")
        print(
            f"Overall scores: positive={doc.confidence_scores.positive}; neutral={doc.confidence_scores.neutral}; negative={doc.confidence_scores.negative}"
        )
        print("\n")


sentiment_analysis_example(client)

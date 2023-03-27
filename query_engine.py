import weaviate
import json

client = weaviate.Client(
    url="http://localhost:8080"
)

nearText = {"concepts": ["biology"]}

result = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text(nearText)
    .with_limit(2)
    .do()
)

print(json.dumps(result, indent=4))

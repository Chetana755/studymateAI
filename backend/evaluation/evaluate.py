import sys
import os
import json

# Allow imports from backend/
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from dotenv import load_dotenv
from google import genai

from ragas import EvaluationDataset, evaluate
from ragas.llms import llm_factory
from ragas.embeddings import GoogleEmbeddings
from ragas.metrics.collections import (
    Faithfulness,
    AnswerRelevancy,
)

from services.rag_service import ask_question


# -----------------------------------------
# 1. Load environment variables
# -----------------------------------------

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError(
        "GEMINI_API_KEY is not set in your .env file"
    )


# -----------------------------------------
# 2. Create Gemini client
# -----------------------------------------

client = genai.Client(
    api_key=gemini_api_key
)


# -----------------------------------------
# 3. Create RAGAS evaluator LLM
# -----------------------------------------

evaluator_llm = llm_factory(
    "gemini-3.6-flash",
    provider="google",
    client=client
)


# -----------------------------------------
# 4. Create RAGAS evaluator embeddings
# -----------------------------------------

evaluator_embeddings = GoogleEmbeddings(
    client=client,
    model="gemini-embedding-001"
)


# -----------------------------------------
# 5. Load evaluation dataset
# -----------------------------------------

dataset_path = os.path.join(
    os.path.dirname(__file__),
    "dataset.json"
)

with open(
    dataset_path,
    "r",
    encoding="utf-8"
) as f:
    evaluation_data = json.load(f)


# -----------------------------------------
# 6. Run StudyMate RAG
# -----------------------------------------

samples = []

for item in evaluation_data:

    print("\n--------------------------------")
    print(f"Evaluating: {item['question']}")
    print("--------------------------------")

    result = ask_question(
        question=item["question"],
        mode="normal"
    )

    samples.append(
        {
            "user_input": item["question"],

            # ChromaDB + BM25 retrieved chunks
            "retrieved_contexts": result[
                "retrieved_contexts"
            ],

            # Gemini-generated answer
            "response": result["answer"],

            # Expected answer
            "reference": item["ground_truth"],
        }
    )


# -----------------------------------------
# 7. Create RAGAS dataset
# -----------------------------------------

dataset = EvaluationDataset.from_list(
    samples
)

print("\n================================")
print("RAGAS DATASET READY")
print("================================")

print(
    f"Number of questions: {len(samples)}"
)


# -----------------------------------------
# 8. Create evaluation metrics
# -----------------------------------------

faithfulness = Faithfulness(
    llm=evaluator_llm
)

answer_relevancy = AnswerRelevancy(
    llm=evaluator_llm,
    embeddings=evaluator_embeddings
)


# -----------------------------------------
# 9. Run evaluation
# -----------------------------------------

print("\n================================")
print("Running RAGAS evaluation...")
print("================================")



# -----------------------------------------
# 10. Display results
# -----------------------------------------

print("\n================================")
print("StudyMate AI Evaluation Results")
print("================================")

print(result)
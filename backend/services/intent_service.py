def detect_intent(question):
    question = question.lower()

    if "quiz" in question or "mcq" in question:
        return "quiz"

    if "flashcard" in question:
        return "flashcards"

    if "summary" in question or "summarize" in question:
        return "summary"

    if "compare" in question or "difference" in question:
        return "comparison"

    if "beginner" in question or "simple" in question:
        return "beginner"

    if (
        "exam" in question
        or "5 mark" in question
        or "10 mark" in question
        or "15 mark" in question
        or "detailed" in question
    ):
        return "exam"

    return "normal"
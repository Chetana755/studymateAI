import { useState } from "react";
import api from "../services/api";

function ChatBox({ setAnswer, setSources, setRetrieval }) {
  const [question, setQuestion] = useState("");
  const [mode, setMode] = useState("normal");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) {
      return;
    }

    try {
      setLoading(true);

      const res = await api.post("/chat", {
        question: question,
        mode: mode,
      });

      setAnswer(res.data.answer);

      setSources(res.data.sources || []);

      setRetrieval(res.data.retrieval || null);
    } catch (err) {
      console.error(err);
      alert("Failed to get answer");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Ask a Question</h2>

      <textarea
        rows="4"
        cols="80"
        placeholder="Ask anything about your study material..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <br />
      <br />

      <label>
        <strong>Study Mode: </strong>
      </label>

      <select value={mode} onChange={(e) => setMode(e.target.value)}>
        <option value="normal">Normal</option>

        <option value="summary">Summary</option>

        <option value="exam">Exam</option>

        <option value="quiz">Quiz</option>
      </select>

      <br />
      <br />

      <button onClick={askQuestion} disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </button>
    </div>
  );
}

export default ChatBox;

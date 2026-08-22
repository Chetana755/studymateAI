import { useState } from "react";
import FileUpload from "../components/FileUpload";
import ChatBox from "../components/ChatBox";
import AnswerCard from "../components/AnswerCard";

function Home() {
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [retrieval, setRetrieval] = useState(null);

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "40px auto",
        padding: "20px",
        fontFamily: "Arial",
      }}
    >
      <h1>📚 StudyMate AI</h1>

      <p>RAG Based AI Study Assistant</p>

      {/* PDF Upload */}
      <FileUpload />

      <hr style={{ margin: "30px 0" }} />

      {/* Question + Study Mode */}
      <ChatBox
        setAnswer={setAnswer}
        setSources={setSources}
        setRetrieval={setRetrieval}
      />

      <hr style={{ margin: "30px 0" }} />

      {/* Answer */}
      <AnswerCard answer={answer} sources={sources} />

      {/* Retrieval Information */}
      {retrieval && (
        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            border: "1px solid #ddd",
            borderRadius: "8px",
            backgroundColor: "#f8f8f8",
          }}
        >
          <h3>🔎 Retrieval Information</h3>

          <p>
            <strong>Semantic Results:</strong> {retrieval.semantic_results}
          </p>

          <p>
            <strong>Keyword Results:</strong> {retrieval.keyword_results}
          </p>

          <p>
            <strong>Combined Results:</strong> {retrieval.combined_results}
          </p>
        </div>
      )}
    </div>
  );
}

export default Home;

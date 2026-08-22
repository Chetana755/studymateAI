import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function AnswerCard({ answer, sources }) {
  return (
    <div>
      <h2>Answer</h2>

      <div
        style={{
          border: "1px solid #ddd",
          borderRadius: "12px",
          padding: "20px",
          backgroundColor: "#ffffff",
          lineHeight: "1.6",
        }}
      >
        {/* Answer */}
        {!answer ? (
          <p>Your answer will appear here.</p>
        ) : (
          <div
            style={{
              fontSize: "16px",
            }}
          >
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                h1: ({ children }) => (
                  <h1 style={{ marginTop: "20px" }}>{children}</h1>
                ),

                h2: ({ children }) => (
                  <h2 style={{ marginTop: "20px" }}>{children}</h2>
                ),

                h3: ({ children }) => (
                  <h3 style={{ marginTop: "18px" }}>{children}</h3>
                ),

                p: ({ children }) => (
                  <p style={{ margin: "10px 0" }}>{children}</p>
                ),

                ul: ({ children }) => (
                  <ul
                    style={{
                      paddingLeft: "25px",
                      margin: "10px 0",
                    }}
                  >
                    {children}
                  </ul>
                ),

                ol: ({ children }) => (
                  <ol
                    style={{
                      paddingLeft: "25px",
                      margin: "10px 0",
                    }}
                  >
                    {children}
                  </ol>
                ),

                li: ({ children }) => (
                  <li
                    style={{
                      marginBottom: "6px",
                    }}
                  >
                    {children}
                  </li>
                ),

                code: ({ children, className }) => {
                  const isCodeBlock = className?.includes("language-");

                  if (isCodeBlock) {
                    return (
                      <code
                        className={className}
                        style={{
                          display: "block",
                          backgroundColor: "#f4f4f4",
                          padding: "15px",
                          borderRadius: "8px",
                          overflowX: "auto",
                          fontFamily: "Consolas, monospace",
                          fontSize: "14px",
                          whiteSpace: "pre",
                        }}
                      >
                        {children}
                      </code>
                    );
                  }

                  return (
                    <code
                      style={{
                        backgroundColor: "#f1f1f1",
                        padding: "2px 5px",
                        borderRadius: "4px",
                        fontFamily: "Consolas, monospace",
                      }}
                    >
                      {children}
                    </code>
                  );
                },

                pre: ({ children }) => (
                  <pre
                    style={{
                      backgroundColor: "#f4f4f4",
                      padding: "15px",
                      borderRadius: "8px",
                      overflowX: "auto",
                      margin: "15px 0",
                    }}
                  >
                    {children}
                  </pre>
                ),

                blockquote: ({ children }) => (
                  <blockquote
                    style={{
                      borderLeft: "4px solid #888",
                      paddingLeft: "15px",
                      marginLeft: "0",
                      color: "#555",
                    }}
                  >
                    {children}
                  </blockquote>
                ),

                hr: () => (
                  <hr
                    style={{
                      margin: "20px 0",
                      border: "none",
                      borderTop: "1px solid #ddd",
                    }}
                  />
                ),
              }}
            >
              {answer}
            </ReactMarkdown>
          </div>
        )}

        <hr
          style={{
            margin: "25px 0",
            border: "none",
            borderTop: "1px solid #ddd",
          }}
        />

        {/* Sources */}
        <h3>Sources</h3>

        {sources.length === 0 ? (
          <p>No sources</p>
        ) : (
          <div>
            {sources.map((source, index) => (
              <div
                key={index}
                style={{
                  padding: "8px 0",
                  borderBottom:
                    index !== sources.length - 1 ? "1px solid #eee" : "none",
                }}
              >
                📄 <strong>{source.source}</strong>
                {" — "}
                Chunk {source.chunk}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default AnswerCard;

import { useState } from "react";
import api from "../services/api";

function FileUpload() {
  const [file, setFile] = useState(null);

  const uploadFile = async () => {
    if (!file) {
      alert("Please select a PDF");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {
      const res = await api.post("/upload", formData);

      alert(res.data.message);
    } catch (err) {
      console.error(err);
      alert("Upload failed");
    }
  };

  return (
    <div>
      <h2>Upload Notes</h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={uploadFile}>Upload PDF</button>
    </div>
  );
}

export default FileUpload;

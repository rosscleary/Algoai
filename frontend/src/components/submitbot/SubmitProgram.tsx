import React, { useState } from "react";
import "./SubmitProgram.css";
import axios from "axios";

const SubmitProgram = () => {
  const [code, setCode] = useState("");
  const [accuracy, setAccuracy] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    await axios
    .post("http://127.0.0.1:5000/processProgram", {
      program: code,
    })
    .then(function (response) {
      setAccuracy(response.data.accuracy);
    })
    .catch(function () {
      return "Failed to test program.";
    });
  };

  return (
    <form id="submitForm" onSubmit={handleSubmit}>
      <div id="textArea">
        <textarea
          id="textField"
          value={code}
          onChange={(e) => setCode(e.target.value)}
          placeholder="Type code here..."
        ></textarea>
      </div>
      <button id="submitButton">
        Submit Program
      </button>
      { accuracy }
    </form>
  );
};

export default SubmitProgram;

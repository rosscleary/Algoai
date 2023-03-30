import React, { useState } from "react";
import "./SubmitProgram.css";
import axios from "axios";

const SubmitProgram = () => {
  const [code, setCode] = useState("");
  const [inputLow, setInputLow] = useState("");
  const [inputHigh, setInputHigh] = useState("");
  const [runCount, setRunCount] = useState("");
  const [randomForestAccuracy, setRandomForestAccuracy] = useState("");
  const [linearRegressionAccuracy, setLinearRegressionAccuracy] = useState("");
  const [neuralNetworkAccuracy, setNeuralNetworkAccuracy] = useState("");

  const starterCode = `#include <bits/stdc++.h>
  using namespace std;
  
  signed main() {
  
  }`;

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setRandomForestAccuracy("Testing program...")
    setLinearRegressionAccuracy("Testing program...")
    setNeuralNetworkAccuracy("Testing program...")
    await axios
    .post("http://127.0.0.1:5000/processProgram", {
      program: code,
      inputLow: inputLow,
      inputHigh: inputHigh,
      runCount: runCount,
    })
    .then(function (response) {
      setRandomForestAccuracy(String(response.data.randomforest));
      setLinearRegressionAccuracy(String(response.data.linearregression));
      setNeuralNetworkAccuracy(String(response.data.neuralnetwork));
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
          value={code ? code : starterCode}
          onChange={(e) => setCode(e.target.value)}
          placeholder="Type code here..."
        ></textarea>
        <textarea
          id="inputField"
          value={inputLow}
          onChange={(e) => setInputLow(e.target.value)}
          placeholder="Type input low here..."
        ></textarea>
        <textarea
          id="inputField"
          value={inputHigh}
          onChange={(e) => setInputHigh(e.target.value)}
          placeholder="Type input high here..."
        ></textarea>
        <textarea
          id="inputField"
          value={runCount}
          onChange={(e) => setRunCount(e.target.value)}
          placeholder="Type run count here..."
        ></textarea>
      </div>
      <button id="submitButton">
        Submit Program
      </button>
      Random Forest Accuracy: { randomForestAccuracy }
      <br></br>
      Linear Regression Accuracy: { linearRegressionAccuracy }
      <br></br>
      Neural Network Accuracy: { neuralNetworkAccuracy }
    </form>
  );
};

export default SubmitProgram;

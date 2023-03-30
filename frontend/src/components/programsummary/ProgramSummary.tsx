import { useState, useEffect } from "react";
import axios from "axios";

export interface Program {
    id: number;
    sourceCode: string;
    language: string;
    version: string;
    inputLow: number;
    inputHigh: number;
    runCount: number;
    randomForestAccuracy: number;
    linearRegressionAccuracy: number;
    neuralNetworkAccuracy: number;
}

const ProgramSummary = () => {
    const [programs, setPrograms] = useState<Program[]>([]);

    useEffect(() => {
        const getPrograms = async () => {
            await axios
            .get("http://127.0.0.1:5000/programs")
            .then(function (response) {
                setPrograms(response.data.programs);
            })
            .catch(function () {
                return "Failed to fetch programs.";
            });
        };
        getPrograms();
    }, []);

    return (
        <div>
            <h1>Programs</h1>
            <ul>
                {programs.map((program) => (
                    <li key={program.id}>
                        <h2>{program.language}</h2>
                        <h2>{program.version}</h2>
                        <p>{program.sourceCode}</p>
                        <p>{program.inputLow}</p>
                        <p>{program.inputHigh}</p>
                        <p>{program.runCount}</p>
                        <p>{program.randomForestAccuracy}</p>
                        <p>{program.linearRegressionAccuracy}</p>
                        <p>{program.neuralNetworkAccuracy}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProgramSummary;
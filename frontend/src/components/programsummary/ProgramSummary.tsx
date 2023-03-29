import { useState, useEffect } from "react";
import axios from "axios";

export interface Program {
    id: number;
    sourceCode: string;
    language: string;
    version: string;
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
                        <p>{program.sourceCode}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProgramSummary;
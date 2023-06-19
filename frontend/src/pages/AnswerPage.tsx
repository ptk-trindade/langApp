import React, { useState } from "react";

import Button from "../components/Button";
import Input from "../components/Input";
import Feedback from "../components/Feedback";

const AnswerPage:React.FC = () => {
    const [answer, setAnswer] = useState("");
    const [feedback, setFeedback] = useState("");

    const possibleAnswers = [
        "Você pode me ajudar?",
        "Você pode me ajudar",
        "você pode me ajudar?",
        "você pode me ajudar"
    ];

    const onSubmit = () => {
        if (possibleAnswers.includes(answer)) {
            setFeedback("right");
        } else {
            setFeedback("wrong");
        }; 
    };

    const showFeedback = () => {
        switch (feedback) {
            case "right":
                return (
                    <Feedback type={feedback}>
                        <p style={{ textAlign: "center", marginTop: 16 }}>
                            <span style={{ fontWeight: "bold", color: "#FD8087" }}>
                                Parabéns!{" "} 
                            </span>
                            Você está correto, a tradução para “Can you help me?” pode ser "{answer}"
                        </p>
                    </Feedback>
                );
            case "wrong":
                return (
                    <Feedback type={feedback}>
                        <p style={{ textAlign: "center", marginTop: 16 }}>
                            <span style={{ fontWeight: "bold", color: "#FD8087" }}>
                                Poxa!{" "} 
                            </span>
                            Você está incorreto, a tradução para “Can you help me?” é “{possibleAnswers[0]}”
                        </p>
                    </Feedback>
                );
            default:
                return <Button text="Pronto" additionalStyle={{ width: 320, marginTop: 20 }} onClick={onSubmit} />;
        };
    };

    return (
        <>
            <div style={{ display: "flex", alignItems: "center", flexDirection: "column", color: "#6D6D6D", fontSize: 14 }}>
                <p style={{ marginTop: 120, textAlign: "left", width: 320 }}>
                    Qual a tradução da frase em <span style={{ color: "#FD8087", fontWeight: "bold" }}>Português</span>?
                </p>
                <Input additionalStyle={{ width: 320 }} value={answer} readOnly={feedback !== ""} onChange={setAnswer} />
                {showFeedback()}
            </div>
        </>
    );
};

export default AnswerPage;

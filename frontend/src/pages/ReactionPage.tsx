import React, { useState } from "react";
import { Link } from "react-router-dom";

import ReactionSection from "../components/ReactionSection";
import DifficultyLevel from "../components/DifficultyLevel";
import Button from "../components/Button";

const ReactionPage:React.FC = () => {
    const [dificultReaction, setDificultReaction] = useState<number | undefined>();
    const [themeReaction, setThemeReaction] = useState<number | undefined>();
    return (
        <div style={{ display: "flex", alignItems: "center", flexDirection: "column" }}>
        <p style={{ fontSize: 14, color: "#6D6D6D", marginTop: 120 }}>Qual foi a dificuldade do Card para você?</p>
        <DifficultyLevel state={dificultReaction} setState={setDificultReaction} />
        <p style={{ fontSize: 14, color: "#6D6D6D", marginTop: 40 }}>Você gostou dos temas do Card?</p>
        <ReactionSection state={themeReaction} setState={setThemeReaction} />
        <Button text="Próximo" additionalStyle={{ width: 230, marginTop: 60 }} />
        <p style={{ fontSize: 13, color: "#6D6D6D" }}>Cansou do jogo?{" "} 
            <Link to="/home" style={{ fontWeight: "bold", color: "#8AC9FE", textDecoration: "none" }}>
                Finalizar jogo
            </Link>
        </p>
        </div>
    );
};

export default ReactionPage;

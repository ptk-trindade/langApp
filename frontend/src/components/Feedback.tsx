import React from "react";
import { Link, useNavigate } from "react-router-dom";

import rightIcon from "../assets/rightIcon.svg";
import wrongIcon from "../assets/wrongIcon.svg";
import Button from "./Button";

interface FeedbackProps {
    type: string;
    children: React.ReactNode;
};

const Feedback:React.FC<FeedbackProps> = ({ type, children }) => {
    const navigate = useNavigate();
    const icon = type === "right" ? rightIcon :  wrongIcon;
    return (
        <div style={{ marginTop: 40, width: 320, display: "flex", alignItems: "center", flexDirection: "column"  }}>
            <img 
                src={icon} 
                className="Feecback Icon"
                alt="Feecback Icon" 
            />
            {children}
            <Button text="Próximo" additionalStyle={{ width: 230 }} onClick={() => navigate("/reactionPage")}/>
            <p style={{ fontSize: 13 }}>Cansou do jogo?{" "} 
                <Link to="/home" style={{ fontWeight: "bold", color: "#8AC9FE", textDecoration: "none" }}>
                    Finalizar jogo
                </Link>
            </p>
        </div>
    );
};

export default Feedback;

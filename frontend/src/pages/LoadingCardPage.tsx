import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Lottie from "lottie-react";

import cardsAnimation from "../assets/cardsAnimation.json";

const LoadingCardPage:React.FC = () => {
    const navigate = useNavigate();
    useEffect(() => {
        const timeout = setTimeout(() => {
          navigate("/cardPage"); 
        }, 4000);
    
        return () => {
          clearTimeout(timeout);
        };
    }, [navigate]);
    return (
        <div style={{ display: "flex", alignItems: "center", flexDirection: "column", color: "#6D6D6D" }}>
            <p style={{ fontSize: 30, textAlign: "center", lineHeight: 1.2, marginTop: 100 }}>
                Gerando <span style={{ color: "#FD8087", fontWeight: "bold" }}>Card</span> <span style={{ color: "#8AC9FE", fontWeight: "bold" }}>Personalizado</span>!
            </p>
            <Lottie 
                animationData={cardsAnimation} 
                style={{ width: 369, height: 271 }}
            />
        </div>
    );
};

export default LoadingCardPage;

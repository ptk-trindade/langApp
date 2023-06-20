import React from "react";
import { useNavigate } from "react-router-dom";

import Card from "../components/Card";
import Button from "../components/Button";

const CardPage:React.FC = () => {
    const navigate = useNavigate();
    return (
        <div style={{ display: "flex", alignItems: "center", flexDirection: "column", color: "#6D6D6D" }}>
            <p style={{ fontSize: 16, color: "#6D6D6D", marginTop: 120, fontWeight: "500" }}>
                Preste atenção na frase durante a cena!
            </p>
            <Card additionalStyle={{ width: 380, height: 280, display: "flex", justifyContent: "center", alignItems: "center" }}>
                <iframe 
                    style={{ marginTop: 0, border: 0, borderRadius: 9 }}
                    width="343" height="187" 
                    src="https://www.youtube.com/embed/uOcV_kRhE0Q" 
                    title="YouTube video player" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                />
            </Card>
            <Button text="Pronto" additionalStyle={{ marginTop: 20 }} onClick={() => navigate("/answerPage")} />
        </div>
    );
};

export default CardPage;

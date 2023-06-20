import React from "react";
import { useNavigate } from "react-router-dom";

import Button from "../components/Button";

const HomePage:React.FC = () => {
    const navigate = useNavigate();
    return (
        <div style={{ display: "flex", alignItems: "center", flexDirection: "column" }}>
            <p style={{ fontWeight: "bold", fontSize: 20, color: "#6D6D6D", marginTop: 54 }}>
                Bem vindo ao Babel Cards!
            </p>
            <p style={{ fontSize: 14, color: "#6D6D6D", marginTop: -8, textAlign: "center", width: 300 }}>
                Jogue nosso jogo de <span style={{ color: "#8AC9FE", fontWeight: "bold" }}>cards</span>{" "}
                <span style={{ color: "#FD8087", fontWeight: "bold" }}>interativos</span>, onde você pratica traduções
                e se diverte com trechos de séries, filmes e músicas
            </p>
            <iframe 
                style={{ marginTop: 27, border: 0, borderRadius: 9 }}
                width="342" height="197" 
                src="https://www.youtube.com/embed/wXNnbNa6Mbs" 
                title="YouTube video player" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
            />
            <p style={{ fontSize: 14, color: "#6D6D6D", marginTop: 37, textAlign: "center", width: 300 }}>
                Comece agora e mergulhe na melhor experiência de aprendizado de idiomas de todos os tempos!
            </p>
            <Button text="Iniciar jogo" additionalStyle={{ marginTop: 0 }} onClick={() => navigate("/chooseLang")} />
        </div>
    );
};

export default HomePage;

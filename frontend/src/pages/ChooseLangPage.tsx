import React from "react";
import { useNavigate } from "react-router-dom";
import Select, { StylesConfig } from "react-select";

import Button from "../components/Button";

const ChooseLangPage:React.FC = () => {
    const navigate = useNavigate();
    const targetLangOptions = [
        { value: "1", label: "Inglês" }
    ];
    const sourceLangOptions = [
        { value: "1", label: "Português" }
    ];
    const customStyles: StylesConfig  = {
        control: (provided) => ({
          ...provided,
          width: 320
        })
    };
    return (
        <div style={{ display: "flex", alignItems: "center", flexDirection: "column", color: "#6D6D6D" }}>
            <p style={{ marginTop: 120, textAlign: "left", width: 320 }}>
                Escolha o <span style={{ color: "#FD8087", fontWeight: "bold" }}>Idioma Alvo</span> (aquele que você deseja aprender)
            </p>
            <Select styles={customStyles} options={targetLangOptions} />
            <p style={{ marginTop: 25, textAlign: "left", width: 320 }}>
                E o <span style={{ color: "#8AC9FE", fontWeight: "bold" }}>Idioma Origem</span> (aquele pelo qual você deseja aprender)
            </p>
            <Select styles={customStyles} options={sourceLangOptions} />
            <Button text="Iniciar jogo" additionalStyle={{ width: 320, marginTop: 51 }} onClick={() => navigate("/loadingCardPage")} />
        </div>
    );
};

export default ChooseLangPage;

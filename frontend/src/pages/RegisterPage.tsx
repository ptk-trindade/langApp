import React from "react";
import { useNavigate } from "react-router-dom";

import TitleAndLogo from "../components/TitleAndLogo";
import Input from "../components/Input";
import Button from "../components/Button";

const RegisterPage:React.FC = () => {
  const navigate = useNavigate();
  return (
    <div style={{ display: "flex", alignItems: "center", flexDirection: "column" }}>
      <TitleAndLogo />
      <Input placeholder="Nome de usuário ou email" />
      <Input placeholder="Senha" type="password" additionalStyle={{ marginTop: 6.6 }} />
      <Button additionalStyle={{ marginTop: 22 }} text="Cadastrar" onClick={() => navigate("/login")} />
    </div>
  );
};

export default RegisterPage;

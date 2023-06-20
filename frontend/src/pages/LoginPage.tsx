import React from "react";
import { Link, useNavigate } from "react-router-dom";

import TitleAndLogo from "../components/TitleAndLogo";
import Input from "../components/Input";
import Button from "../components/Button";

const LoginPage:React.FC = () => {
  const navigate = useNavigate();
  return (
    <div style={{ display: "flex", alignItems: "center", flexDirection: "column" }}>
      <TitleAndLogo />
      <Input placeholder="Nome de usuário ou email" />
      <Input placeholder="Senha" additionalStyle={{ marginTop: 6.6 }} type="password" />
      <Button text="Entrar" additionalStyle={{ marginTop: 22 }} onClick={() => navigate("/home")} />
      <p style={{ fontSize: 14, color: "#6D6D6D", marginTop: 6 }}>
        Não tem uma conta?{" "}
        <Link to="/register" style={{ color: "#8AC9FE", fontWeight: "bold", textDecoration: "none" }}>
          Cadastre-se
        </Link>
      </p>   
    </div>
  );
};

export default LoginPage;

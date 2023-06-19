import React from "react";

import TitleAndLogo from "../components/TitleAndLogo";
import { Link } from "react-router-dom";

const InitialPage:React.FC = () => {
  return (
    <div style={{ display: "flex", alignItems: "center", flexDirection: "column" }}>
      <TitleAndLogo />
      <p style={{ marginTop: -20, width: 290, textAlign: "center" }}>
        Cadastre-se e descubra uma nova forma envolvente de aprender idiomas!
      </p>
      <p style={{ marginTop: -10, fontSize: 14 }}>
        <Link to="/login" style={{ color: "#FD8087", fontWeight: "bold", textDecoration: "none" }}>
          Entrar
        </Link>{" "}
        ou{" "}
        <Link to="/register" style={{ color: "#FD8087", fontWeight: "bold", textDecoration: "none" }}>
          cadastrar-se
        </Link>
      </p>
    </div>
  )

};

export default InitialPage;

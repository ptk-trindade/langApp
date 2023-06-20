import React from "react";

import babelCardsLogo from "../assets/babelCardsLogo.svg";

const TitleAndLogo:React.FC = () => {
  return (
    <>
      <img 
        src={babelCardsLogo} 
        className="Logo babel cards" 
        alt="Babel Cards Logo" 
        style={{ marginTop: 121, width: 152 }}
      />
      <p style={{ fontWeight: "bold", fontSize: 30, marginTop: 0 }}>Babel Cards</p>
    </>
  )

};

export default TitleAndLogo;

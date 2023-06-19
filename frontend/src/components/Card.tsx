import React from "react";

interface CardProps {
  children: React.ReactNode;
  additionalStyle?: React.CSSProperties;
}

const Card: React.FC<CardProps> = ({ children, additionalStyle }) => {
  return (
    <div
      style={{
        boxSizing: "border-box",
        width: 246,
        height: 389,
        background: "#FD8087",
        border: "10.892px solid #000000",
        boxShadow: "0px 4.80449px 4.80449px rgba(0, 0, 0, 0.25)",
        borderRadius: 53,
        ...additionalStyle
      }}
    >
      {children}
    </div>
  );
};

export default Card;
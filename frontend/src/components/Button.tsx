import React from "react";

interface ButtonProps {
    text: string;
    onClick?: React.MouseEventHandler<HTMLButtonElement>;
    additionalStyle?: React.CSSProperties;
}

const Button:React.FC<ButtonProps> = ({ text, onClick, additionalStyle }) => {
  return (
    <button 
        style={{
            width: 230,
            height: 40,
            background: "#8AC9FE",
            borderRadius: 6.6,
            fontSize: 14,
            color: "#fff",
            fontWeight: "bold",
            cursor: "pointer",
            border: 0,
            ...additionalStyle
        }}
        onClick={onClick}
    >
        {text}
    </button>
  );
};

export default Button;

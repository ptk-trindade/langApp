import React from "react";

interface InputProps {
    placeholder?: string;
    additionalStyle?: React.CSSProperties;
    value?: string;
    onChange?: React.Dispatch<React.SetStateAction<string>>;
    readOnly?: boolean;
    type?: string;
}

const Input:React.FC<InputProps> = ({ placeholder, additionalStyle, value, onChange, readOnly, type }) => {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (onChange) {
      onChange(e.target.value);
    };
  };
  return (
    <input 
        style={{
            boxSizing: "border-box",
            width: 230,
            height: 40,
            background: "#FAFAFA",
            border: "1.32031px solid #E1E1E1",
            borderRadius: "3.30078px",
            padding: "0 10px",
            fontSize: 12,
            color: "#6C6C6C",
            fontWeight: "500",
            outline: "none",
            ...additionalStyle
        }}
        placeholder={placeholder}
        value={value}
        onChange={handleChange}
        readOnly={readOnly}
        type={type}
    />
  );
};

export default Input;

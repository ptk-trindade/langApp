import React from "react";

import easyIcon from "../assets/easyIcon.svg";
import mediumIcon from "../assets/mediumIcon2.svg";
import hardIcon from "../assets/hardIcon.svg";

interface ReactionSectionProps {
  state: number | undefined;
  setState: React.Dispatch<React.SetStateAction<number | undefined>>;
}

const ReactionSection: React.FC<ReactionSectionProps> = ({ state, setState }) => {
  const handleClick = (index: number) => {
    setState(index);
  };

  return (
    <div>
      <img
        onClick={() => handleClick(1)}
        src={easyIcon}
        style={{
          width: "80px",
          height: "60px",
          marginRight: 15,
          opacity: state === 1 ? 1 : 0.4,
          cursor: "pointer",
        }}
        alt="Easy Difficulty"
      />
      <img
        onClick={() => handleClick(2)}
        src={mediumIcon}
        style={{
          width: "80px",
          height: "60px",
          opacity: state === 2 ? 1 : 0.4,
          cursor: "pointer",
        }}
        alt="Medium Difficulty"
      />
      <img
        onClick={() => handleClick(3)}
        src={hardIcon}
        style={{
          width: "80px",
          height: "60px",
          marginLeft: 15,
          opacity: state === 3 ? 1 : 0.4,
          cursor: "pointer",
        }}
        alt="Hard Difficulty"
      />
    </div>
  );
};

export default ReactionSection;

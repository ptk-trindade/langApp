import React from "react";

import happyIcon from "../assets/happyIcon.svg";
import mediumIcon from "../assets/mediumIcon.svg";
import sadIcon from "../assets/sadIcon.svg";

interface ReactionSectionProps {
    state: number | undefined;
    setState: React.Dispatch<React.SetStateAction<number | undefined>>;
};

const ReactionSection:React.FC<ReactionSectionProps> = ({ state, setState }) => {
    const handleClick = (index: number) => {
        setState(index)
    };
    return (
        <div>
            <img onClick={() => handleClick(1)} src={happyIcon} style={{ marginRight: 15, opacity: state === 1 ? 1 : 0.4, cursor: "pointer" }} />
            <img onClick={() => handleClick(2)} src={mediumIcon} style={{ opacity: state === 2 ? 1 : 0.4, cursor: "pointer" }} />
            <img onClick={() => handleClick(3)} src={sadIcon} style={{ marginLeft: 15, opacity: state === 3 ? 1 : 0.4, cursor: "pointer" }} />
        </div>
  );
};

export default ReactionSection;

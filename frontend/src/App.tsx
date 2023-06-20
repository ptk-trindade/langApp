import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from "./pages/HomePage";
import InitialPage from "./pages/InititalPage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import ChooseLangPage from "./pages/ChooseLangPage";
import LoadingCardPage from "./pages/LoadingCardPage";
import CardPage from "./pages/CardPage";
import AnswerPage from "./pages/AnswerPage";
import ReactionPage from "./pages/ReactionPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<InitialPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/chooseLang" element={<ChooseLangPage />} />
        <Route path="/loadingCardPage" element={<LoadingCardPage />} />
        <Route path="/cardPage" element={<CardPage />} />
        <Route path="/answerPage" element={<AnswerPage />} />
        <Route path="/reactionPage" element={<ReactionPage />} />
      </Routes>
    </Router>
  );
};

export default App;

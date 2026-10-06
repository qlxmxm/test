import React from "react";
import Greet from "./components/Greet";

const App = () => {
  return (
    <div>
      <h1>인사하기</h1>
      <Greet name='hi'></Greet>
    </div>
  );
};

export default App;


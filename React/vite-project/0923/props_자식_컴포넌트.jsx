import React from 'react';
import Button from "./components/Button";

const App = () => {

  return (
    <>
      <Button message={"리액트"} color={"pink"}/>
      <Button message={"DB"} />
      <Button message={"FAST API"} />
    </>
  );
};

export default App;
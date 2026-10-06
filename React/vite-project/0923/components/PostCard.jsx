import React from "react";

const PostCard = (props) => {
  return (
    <div style={{ border: "1px solid gray", padding: "10px", margin: "10px" }}>
      <h3>{props.title}</h3>
      <p>{props.content}</p>
    </div>
  );
};

export default PostCard;
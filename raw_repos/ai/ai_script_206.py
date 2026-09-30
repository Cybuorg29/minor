import React, { useState } from 'react';

const Form = () => {
  const [input, setInput] = useState('');
  const handleSubmit = (e) => {
    e.preventDefault();
    // Do something with input
  }
  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={input} onChange={e => setInput(e.target.value)} />
      <button type="submit">Submit</button>
    </form>
  )
};

export default Form;
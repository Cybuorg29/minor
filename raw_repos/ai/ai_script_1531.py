import React, { useState, useEffect } from 'react';

function Table(props) {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('https://example.com/data.json')
      .then(response => response.json())
      .then(json => setData(json))
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Age</th>
          <th>Job</th>
        </tr>
      </thead>
      <tbody>
        {data.map(item => (
          <tr>
            <td>{item.name}</td>
            <td>{item.age}</td>
            <td>{item.job}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Table;
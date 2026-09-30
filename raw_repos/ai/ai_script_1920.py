import React from 'react';

const dataTable = props => {
  const { data } = props;

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
        { data.map(item => (
          <tr>
            <td>{item.name}</td>
            <td>{item.age}</td>
            <td>{item.job}</td>
          </tr>
        )) }
      </tbody>
    </table>
  );
}

export default dataTable;
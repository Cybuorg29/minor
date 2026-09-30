import React from 'react';

class Table extends React.Component {
  render() {
    const state = this.props.state;
    const dataRows = state.data.map(rowData => (
      <tr>
        <td>{rowData.name}</td>
        <td>{rowData.age}</td>
      </tr>
    ));

    return (
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>{dataRows}</tbody>
      </table>
    );
  }
}
export default Table;
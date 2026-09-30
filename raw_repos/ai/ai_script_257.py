import React from 'react';

const ListItems = props => {
  const items = props.listItems.map(item => (
    <li key={item}>{item}</li>
  ));

  return (
    <ul>
      {items}
    </ul>
  );
};

export default ListItems;
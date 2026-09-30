import React from 'react';

class SortComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      strings: this.props.strings
    };
  }
  
  // sorting function
  sort = (strings) => {
    return strings.sort();
  }
  
  render() {
    let sortedStrings = this.sort(this.state.strings);
    return (
      <div>
        <div>Sorted strings: </div>
        {sortedStrings.map((str) => <div>{str}</div>)}
      </div>
    );
  }
}

// Usage
<SortComponent strings={["test", "data", "string"]} />
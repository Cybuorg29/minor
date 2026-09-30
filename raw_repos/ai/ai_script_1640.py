import React from 'react';

class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      visible: false
    };
  }

  handleClick = () => {
    this.setState({ visible: !this.state.visible });
  }

  render () {
    return (
      <div>
        <button onClick={this.handleClick}>Toggle</button>
        {this.state.visible && <p>Some text.</p>}
      </div>
    );
  }
}

export default Toggle;
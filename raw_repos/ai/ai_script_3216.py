import React from 'react';

class CurrentTime extends React.Component {
  render() {
    const date = new Date();
    return (
      <div>
        {date.toLocaleString()}
      </div>
    );
  }
}
export default CurrentTime;
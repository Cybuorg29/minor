class Greeting extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      time: new Date().toLocaleTimeString(), 
    };
  }
  render() {
    return <h3>Good {this.props.timeOfDay}, the current time is {this.state.time}.</h3>;
  }
}
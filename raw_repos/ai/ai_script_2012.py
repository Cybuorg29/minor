import React, { Component } from 'react';

class DropdownMenu extends Component {
  state = {
    displayMenu: false,
  };

  showDropdownMenu = (event) => {
    event.preventDefault();
    this.setState({ displayMenu: true }, () => {
      document.addEventListener('click', this.hideDropdownMenu);
    });
  }

  hideDropdownMenu = () => {
    this.setState({ displayMenu: false }, () => {
      document.removeEventListener('click', this.hideDropdownMenu);
    });
  }

  render() {
    return (
      <div  className="dropdown" style={{background:"#fafafa",boxShadow: "0px 8px 16px 0px rgba(0,0,0,0.2)"}} >
        <div className="button" onClick={this.showDropdownMenu}> Menu </div>
        { this.state.displayMenu ? (
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
        ):
        (
          null
        )
        }
      </div>
    );
  }
}
export default DropdownMenu;
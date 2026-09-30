import React from "react";

const CountryList = ({ countries }) => {
  return (
    <ul>
      {countries.map(country => {
        return <li>{country}</li>;
      })}
    </ul>
  );
};

export default CountryList;
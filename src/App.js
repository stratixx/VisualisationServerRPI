import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {

  constructor(props) {
    super(props);
    console.log("App constructor")
    console.log(this.props);
  }

  buttonInput1() {
    console.log("button input 1 clicked")
  }
  buttonInput2() {
    console.log("button input 2 clicked")
  }
  buttonInput3() {
    console.log("button input 3 clicked")
  }

  render() {
  return <div className="App">


  <table class="GeneratedTable">
    <thead>
      <tr>
        <th>Input</th>
        <th>State</th>
        <th>Output</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <button onClick={this.buttonInput1}>IN1</button>
        </td>
        <td>S1</td>
        <td>OUT1</td>
      </tr>
      <tr>
        <td>
          <button onClick={this.buttonInput2}>IN2</button>
        </td>
        <td>S2</td>
        <td>OUT2</td>
      </tr>
      <tr>
        <td>
          <button onClick={this.buttonInput3}>IN3</button>
        </td>
        <td>S3</td>
        <td>OUT3</td>
      </tr>
    </tbody>
  </table>
    </div>
  }
}


export default App;

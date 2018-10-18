import React, { Component } from 'react';


class App extends Component {
  state= {
    zanttas: []
  }
  async componentDidMount(){
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      const zanttas = await res.json();
      this.setState({
        zanttas
      });
    } catch (error) {
      console.log(error);
    }
  }

  render() {
    return (
      <div>
        {this.state.zanttas.map(zantta => (
          <div key={zantta.id}>
            <h1>{zantta.title}</h1>  
            <span>{zantta.description}</span>
          </div>
        ))}
      </div>
        
    );
  }
}

export default App;
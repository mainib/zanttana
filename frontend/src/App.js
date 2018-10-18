import React, { Component } from 'react';


class App extends Component {
  state= {
    zanttas: []
  }
  async componentDidMount(){
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      const zanttas = await res.json();
      console.log(zanttas)
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
            <h1>{zantta.zantta_name}</h1>  
            <span>from {zantta.start_date} to {zantta.end_date}</span>
            <br/>
            <span>{zantta.description}</span>
          </div>
        ))}
      </div>
        
    );
  }
}

export default App;
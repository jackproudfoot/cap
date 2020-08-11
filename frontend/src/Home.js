import React from 'react';
import QueryForm from './QueryForm';

import Grid from '@material-ui/core/Grid'

import capSfx from './res/cap.mp3'
import nocapSfx from './res/no-cap.mp3'

import './Home.css';


class Home extends React.Component {
  constructor(props) {
    super(props)

    this.state = {'query': '', 'result': 'No Cap'}

    this.capRef = React.createRef()
    this.nocapRef = React.createRef()

    this._postCap = this._postCap.bind(this)
    this._handleQueryChange = this._handleQueryChange.bind(this)
  }

  _handleQueryChange(event) {
    this.setState({'query': event.target.value})
  }

  _postCap(event) {
    if (this.state.query == '') return

    console.log('post request')

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ input: this.state.query })
    };

    fetch('http://localhost:5000/cap', requestOptions)
      .then(response => response.json())
      .then(data => {
        console.log(data)

        this.setState({'result': data.response})

        if (this.state.result.substring(0, 2) == 'no') {
          this.nocapRef.current.play()
        }
        else {
          this.capRef.current.play()
        }

        
      });
  }

  render() {
    return (
      <div className="Home">
        <Grid container justify='center' alignItems='center' spacing={4} direction='column' className='HomeGrid'>
            <Grid item className='QueryFormItem'>
              <QueryForm handleQueryChange={this._handleQueryChange} result={this.state.result} />
            </Grid>
            <Grid item className='GridButton'>
              <button className="CapButton" onClick={this._postCap}>Cap or No Cap</button>
            </Grid>
        </Grid>
        <div className="HomeFooter">A Crawdads Production ©2020</div>
        
        
        <audio ref={this.capRef} src={capSfx} hidden ></audio>
        <audio ref={this.nocapRef} src={nocapSfx} hidden ></audio>
      </div>
    );
  }
}

export default Home;

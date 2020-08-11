import React from 'react';
import Paper from '@material-ui/core/Paper'

import Grid from '@material-ui/core/Grid'
import Container from '@material-ui/core/Container'

import Typography from '@material-ui/core/Typography'

import './QueryForm.css';

class QueryForm extends React.Component {
  
  constructor(props) {
    super(props);
  }
  
  render() {
    var resultFontsize = this.props.result.length > 8 ? this.props.result.length > 12 ? 50 : 60 : 80;

    return (
        <Paper elevation={2} square={false}>
            <Container className='QueryCard'>
                <Grid container justify='flex-start' alignItems='center' direction="row" spacing={1} className='QueryCardGrid'>
                    <Grid item xs={12} className="QueryGridItem">
                        <textarea style={{ fontSize: '30px', boxSizing: 'border-box', padding: '20px'}} placeholder="Enter your statement" className='QueryCardTextArea' onChange={this.props.handleQueryChange}></textarea> 
                    </Grid>
                    <Grid item xs={12} className="ResultGridItem">
                        <Typography style={{ fontSize: resultFontsize, fontWeight: 'bold'}} className="QueryCardResultText">{this.props.result}</Typography>
                    </Grid>
                </Grid>
            </Container>
        </Paper>
    );
  }
}

export default QueryForm;

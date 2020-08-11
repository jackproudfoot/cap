import React from 'react';
import Home from './Home';

import { createMuiTheme } from '@material-ui/core/styles';
import { ThemeProvider } from '@material-ui/styles';

import './App.css';

const theme = createMuiTheme({
  typography: {
    fontFamily: [
      'Comic Sans MS',
      'sans-serif'
    ].join(','),
  }
});

/*class App extends Component {
  render() {
    return (
      <ThemeProvider theme={theme}>
        <Switch>
          <Route exact path="/" component={Home} />
        </Switch>
      </ThemeProvider>
    );
  }
}

export default App;*/
function App() {
  return (
    <ThemeProvider theme={theme}>
        <Home />
    </ThemeProvider>
  );
}

export default App;

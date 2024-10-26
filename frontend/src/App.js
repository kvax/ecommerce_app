import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Catalog from './components/Catalog';
import Order from './components/Order';
import Admin from './components/Admin';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token'));

  const saveToken = (userToken) => {
    localStorage.setItem('token', userToken);
    setToken(userToken);
  };

  return (
    <Router>
      <Switch>
        {!token ? (
          <Route exact path="/">
            <Login setToken={saveToken} />
          </Route>
        ) : (
          <>
            <Route exact path="/catalog">
              <Catalog token={token} />
            </Route>
            <Route exact path="/orders">
              <Order token={token} />
            </Route>
            <Route exact path="/admin">
              <Admin token={token} />
            </Route>
          </>
        )}
      </Switch>
    </Router>
  );
}

export default App;

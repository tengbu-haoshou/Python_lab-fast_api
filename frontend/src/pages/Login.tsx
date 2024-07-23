import {Grid, Box, Button, TextField} from '@mui/material';
import CssBaseline from '@mui/material/CssBaseline';

import {useNavigate} from "react-router-dom";
import {useState, useEffect, useRef} from 'react';

import Header from './components/Header';
import Footer from './components/Footer';
import Logout from './components/Logout';

const styles = {
  marginLeft: 1, marginRight: 0,
};

function Login() {
  const [message, setMessage] = useState('');
  const [userName, setUserName] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  const loaded = useRef(false);
  useEffect(() => {
    if (loaded.current) {
      return;
    }
    loaded.current = true;
    Logout();
  }, []);
  const login = async () => {
    if (! userName) {
      setMessage('User Name is required.');
      return;
    }
    if (! password) {
      setMessage('Password is required.');
      return;
    }
    const headers = new Headers();
    const formData = new FormData();
    formData.append('username', userName);
    formData.append('password', password);
    const request = new Request('http://localhost:3001/auth', {
      method: 'POST',
      headers: headers,
      body: formData,
      credentials: 'include',
    });
    let error = false;
    await fetch(request)
    .then (response => {
      if (! response.ok) {
        error = true;
      }
      return response.json();
    })
    .then (data => {
      if (error) {
        setMessage('User Name or Password is invalid.');
        return;
      }
      const token = data.access_token;
      navigate('/home');
    })
    .catch (error => {
      setMessage('Network trouble has occurred.');
      return;
    });
  }
  return (
    <>
      <CssBaseline />
      <Header logoutButton={false}/>
      <Box
        component="form" noValidate autoComplete="off"
        display='flex'
        flexDirection='column'
        justifyContent='space-between'
        sx={{'& .MuiTextField-root': {m: 1, width: '30ch'}}}
      >
        <Grid sx={styles}>
          <h3>Login</h3>
        </Grid>
        <Grid sx={styles}>
          {message}
        </Grid>
        <Grid item xs={16}>
          <TextField id="userName" label="User Name" variant="outlined" onChange={(e) => setUserName(e.target.value)} />
        </Grid>
        <Grid item xs={16}>
          <TextField id="password" label="Password" type="password" autoComplete="" onChange={(e) => setPassword(e.target.value)} />
        </Grid>
        <Grid sx={styles}>
          <Button variant="contained" color="primary" onClick={login} sx={{textTransform: "none"}}>Login</Button>
        </Grid>
      </Box>
      <Footer />
    </>
  );
}

export default Login;

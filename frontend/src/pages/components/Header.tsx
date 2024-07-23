import React from 'react';
import {AppBar, Toolbar, Typography, Button} from '@mui/material';

import Logout from './Logout';

import {useNavigate} from "react-router-dom";

function Header({logoutButton = true}) {
  const navigate = useNavigate();
  function logout() {
    Logout();
    navigate('/login');
  }
  return (
    <>
      <AppBar component="header" position="fixed">
        <Toolbar>
          <Typography variant="caption" sx={{flexGrow: 1, display: {xs: 'none', sm: 'block'}}}><h1>Lab FastAPI</h1></Typography>
          {logoutButton && (
            <Button variant="contained" color="primary" onClick={logout} sx={{textTransform: "none"}}>Logout</Button>
          )}
        </Toolbar>
      </AppBar>
      <br />
      <br />
      <br />
    </>
  )
}

export default Header;

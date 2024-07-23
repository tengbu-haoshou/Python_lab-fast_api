import {Grid, Box, Tabs, Tab} from '@mui/material';
import CssBaseline from '@mui/material/CssBaseline';

import {useNavigate} from "react-router-dom";
import {useState, useEffect, useRef} from 'react';

import Header from './components/Header';
import Footer from './components/Footer';

const styles = {
  marginLeft: 1, marginRight: 0,
};

function Settings() {
  const [message, setMessage] = useState('');
  const emptyData: {no: number, message: string}[] = [];
  const [data, setData] = useState(emptyData);
  const navigate = useNavigate();
  const isValid: () => void = async () => {
    const headers = new Headers();
    const request = new Request('http://localhost:3001/is_valid', {
      method: 'POST',
      headers: headers,
      credentials: 'include',
    });
    let error = false
    await fetch(request)
    .then (response => {
      if (! response.ok) {
        error = true;
        return {
          response: {
            status: 'action-ng',
            message: 'Session timeout has occurred.',
          },
        };
      }
      return response.json();
    })
    .then (data => {
      if (error) {
        setMessage(data.response.message);
        return;
      }
      setData([
        {no: 1, message: '設定画面です。'},
        {no: 2, message: '設定画面です。'},
        {no: 3, message: '設定画面です。'},
        {no: 4, message: '設定画面です。'},
        {no: 5, message: '設定画面です。'},
        {no: 6, message: '設定画面です。'},
        {no: 7, message: '設定画面です。'},
        {no: 8, message: '設定画面です。'},
        {no: 9, message: '設定画面です。'},
        {no: 10, message: '設定画面です。'},
      ]);
    })
    .catch (error => {
      setMessage('Network trouble has occurred.');
      return;
    });
  }
  const loaded = useRef(false);
  useEffect(() => {
    if (loaded.current) {
      return;
    }
    loaded.current = true;
    isValid();
  }, []);
  function gotoHome() {
    navigate('/home');
    return;
  };
  function gotoSettings() {
    navigate('/settings');
    return;
  };
  return (
    <>
      <CssBaseline />
      <Header />
      <Box
        component="form" noValidate autoComplete="off"
        display='flex'
        flexDirection='column'
        justifyContent='space-between'
        sx={{'& .MuiTextField-root': {m: 1, width: '30ch'}}}
      >
        <Grid sx={styles}>
          <Tabs value="Settings">
            <Tab id="home" label="Home" value="Home" sx={{textTransform: "none"}} onClick={gotoHome} />
            <Tab id="settings" label="Settings" value="Settings" style={{fontSize: 18, fontWeight: 'bold'}} sx={{textTransform: "none"}} onClick={gotoSettings} />
          </Tabs>
        </Grid>
        <Grid sx={styles}>
          {message}
        </Grid>
        {message === '' && (
          <Grid sx={styles}>
            <br />
            {data.map(row => (
              <>
                {row.message}<br />
              </>
            ))}
          </Grid>
        )}
      </Box>
      <Footer />
    </>
  );
}

export default Settings;

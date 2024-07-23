import {Grid, Box, Tabs, Tab} from '@mui/material';
import CssBaseline from '@mui/material/CssBaseline';

import {useNavigate} from "react-router-dom";
import {useState, useEffect, useRef} from 'react';

import Header from './components/Header';
import Footer from './components/Footer';

const styles = {
  marginLeft: 1, marginRight: 0,
};

function Home() {
  const [message, setMessage] = useState('');
  const emptyData: {name: string, remark: string}[] = [];
  const [data, setData] = useState(emptyData);
  const navigate = useNavigate();
  const getProducts: () => void = async () => {
    const headers = new Headers();
    const request = new Request('http://localhost:3001/products', {
      method: 'GET',
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
      setData(data.response.list);
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
    getProducts();
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
          <Tabs value="Home">
            <Tab id="home" label="Home" value="Home" style={{fontSize: 18, fontWeight: 'bold'}} sx={{textTransform: "none"}} onClick={gotoHome} />
            <Tab id="settings" label="Settings" value="Settings" sx={{textTransform: "none"}} onClick={gotoSettings} />
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
                {row.name}, {row.remark}<br />
              </>
            ))}
          </Grid>
        )}
      </Box>
      <Footer />
    </>
  );
}

export default Home;

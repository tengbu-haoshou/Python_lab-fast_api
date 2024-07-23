import React from 'react';
import {AppBar, Paper, BottomNavigation, Typography} from '@mui/material';

const styles = {
  marginLeft: 2, marginRight: 2,
};

function Footer() {
  return (
    <>
      <Paper sx={{position: 'fixed', bottom: 0, left: 0, right: 0}}>
        <BottomNavigation>
          <AppBar component="footer" position="static">
            <Typography variant="caption" sx={styles}><h3>Copyright &copy; Xxxx Co., Ltd.</h3></Typography>
          </AppBar>
        </BottomNavigation>
      </Paper>
    </>
  )
}

export default Footer;

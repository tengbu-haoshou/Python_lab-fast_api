import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import Top from './pages/Top';
import Login from './pages/Login';
import Home from './pages/Home';
import Settings from './pages/Settings';

import {BrowserRouter, Route, Routes} from 'react-router-dom';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Top />} />
        <Route path='/login' element={<Login />} />
        <Route path='/home' element={<Home />} />
        <Route path='/settings' element={<Settings />} />
        <Route path='*' element={<h3>Not Found.</h3>} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

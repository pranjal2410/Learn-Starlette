import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter} from "react-router-dom";
import {ThemeContextProvider} from "./context/theme";
import {SnackbarProvider} from "notistack";
import {AuthContextProvider} from "./context/auth";

ReactDOM.render(
    <BrowserRouter>
        <ThemeContextProvider>
            <AuthContextProvider>
                <SnackbarProvider maxSnack={1}>
                    <App />
                </SnackbarProvider>
            </AuthContextProvider>
        </ThemeContextProvider>
    </BrowserRouter>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

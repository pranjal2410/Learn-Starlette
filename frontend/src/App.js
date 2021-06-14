import * as React from "react";
import {ThemeContext} from "./context/theme";
import {
    MuiThemeProvider,
    CssBaseline,
} from "@material-ui/core";
import Routes from "./components/Routes";

const App = () => {
    const {theme} = React.useContext(ThemeContext);
    return (
        <MuiThemeProvider theme={theme}>
            <CssBaseline/>
            <Routes/>
        </MuiThemeProvider>
    )
}

export default App;

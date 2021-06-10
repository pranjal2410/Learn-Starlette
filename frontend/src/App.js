import * as React from "react";
import {ThemeContext} from "./context/theme";
import {MuiThemeProvider, CssBaseline} from "@material-ui/core";

const App = () => {
    const {theme} = React.useContext(ThemeContext);
    return (
        <MuiThemeProvider theme={theme}>
            <CssBaseline/>
        </MuiThemeProvider>
    )
}

export default App;

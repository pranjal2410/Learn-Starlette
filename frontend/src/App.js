import * as React from "react";
import {ThemeContext} from "./context/theme";
import {
    MuiThemeProvider,
    CssBaseline,
    AppBar,
    Toolbar,
    IconButton,
    Typography,
} from "@material-ui/core";
import Routes from "./components/Routes";
import {Brightness4, Brightness7, ExitToApp} from "@material-ui/icons";
import {useHistory} from "react-router";

const App = () => {
    const {theme, toggleTheme} = React.useContext(ThemeContext);
    const history = useHistory();

    const handleLogout = () => {
        sessionStorage.removeItem('token');
        history.push('/')
    }

    return (
        <MuiThemeProvider theme={theme}>
            <CssBaseline/>
            <AppBar position="sticky" color='inherit'>
                <Toolbar>
                    <IconButton onClick={toggleTheme} color='inherit'>
                        {theme.palette.type==='dark'?<Brightness7/>:<Brightness4/>}
                    </IconButton>
                    <Typography variant="h6" color="inherit" noWrap>
                        Blog posting site
                    </Typography>
                    {sessionStorage.getItem('token') && (
                        <IconButton color='inherit' onClick={handleLogout} edge="end">
                            <ExitToApp />
                        </IconButton>
                    )}
                </Toolbar>
            </AppBar>
            <Routes/>
        </MuiThemeProvider>
    )
}

export default App;

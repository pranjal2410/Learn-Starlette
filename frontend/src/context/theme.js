import * as React from "react";
import {createMuiTheme, colors} from "@material-ui/core";

const ThemeContext = React.createContext();

const ThemeContextProvider = (props) => {
    const lightTheme = createMuiTheme({
        palette: {
            type: 'light',
            primary: {
                main: colors.blue[700],
            },
            secondary: {
                main: colors.red[700]
            }
        }
    });

    const darkTheme = createMuiTheme({
        palette: {
            type: 'dark',
            primary: {
                main: colors.blue[300]
            },
            secondary: {
                main: colors.red[300],
            }
        }
    });
    const [theme, setTheme] = React.useState(darkTheme);

    const toggleTheme = () => {
        setTheme(theme.palette.type==='light'?darkTheme:lightTheme);
    }

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {props.children}
        </ThemeContext.Provider>
    )
}

export {ThemeContext, ThemeContextProvider}
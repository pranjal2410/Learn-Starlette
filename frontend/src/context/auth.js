import * as React from "react";
import {getToken} from "../cookies";

const AuthContext = React.createContext();

const AuthContextProvider = (props) => {
    const [auth, setAuth] = React.useState(!!getToken());

    return (
        <AuthContext.Provider value={{ auth, setAuth }}>
            {props.children}
        </AuthContext.Provider>
    )
}

export {AuthContext, AuthContextProvider}
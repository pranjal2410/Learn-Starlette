import * as React from "react";
import {Route, Switch} from "react-router";
import SignUp from "./Users/UserRegistration";

const Routes = () => {
    return (
        <Switch>
            <Route exact path='/'>
                <SignUp/>
            </Route>
        </Switch>
    )
}

export default Routes;
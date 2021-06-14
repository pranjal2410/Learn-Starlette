import * as React from "react";
import {Route, Switch} from "react-router";
import SignUp from "./Users/UserRegistration";
import UserSignIn from "./Users/UserSignIn";

const Routes = () => {
    return (
        <Switch>
            <Route exact path='/'>
                <UserSignIn />
            </Route>
            <Route path='/register'>
                <SignUp />
            </Route>
        </Switch>
    )
}

export default Routes;
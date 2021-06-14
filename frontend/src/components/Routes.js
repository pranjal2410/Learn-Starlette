import * as React from "react";
import {Route, Switch} from "react-router";
import SignUp from "./Users/UserRegistration";
import UserSignIn from "./Users/UserSignIn";
import ViewBlog from "./Blog/ViewBlog";

const Routes = () => {
    return (
        <Switch>
            <Route exact path='/'>
                <UserSignIn />
            </Route>
            <Route path='/register'>
                <SignUp />
            </Route>
            <Route path='/blog'>
                <ViewBlog />
            </Route>
        </Switch>
    )
}

export default Routes;
import React from 'react';
import {LockOutlined} from '@material-ui/icons';
import {
    makeStyles,
    Container,
    Grid,
    Link,
    Checkbox,
    TextField,
    Button,
    Avatar,
    FormControlLabel,
    Typography
} from '@material-ui/core';
import Axios from "axios";
import {useHistory} from "react-router";

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

const UserSignIn = () => {
    const classes = useStyles();
    let history = useHistory();

    const [data, setData] = React.useState({
        username: '',
        password: '',
    });

    const [error, setError] = React.useState(false);

    const handleChange = (event) => {
        setData({
            ...data,
            [event.target.id]: event.target.value
        });
    }

    const handleSubmit = async(event) => {
        event.preventDefault();
        try {
            const response = await Axios.post(`${process.env.REACT_APP_API_URL}/login`, data)
                .then(res => res.data);
            sessionStorage.setItem('token', response.token);
        }
        catch(err) {
            setError(true);
        }
    }

    return (
        <Container component="main" maxWidth="xs">
            <div className={classes.paper}>
                <Avatar className={classes.avatar}>
                    <LockOutlined />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <form className={classes.form} noValidate onSubmit={handleSubmit}>
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="username"
                        label="Username"
                        name="username"
                        autoComplete="username"
                        onChange={handleChange}
                        error={error}
                        autoFocus
                    />
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        error={error}
                        onChange={handleChange}
                        id="password"
                        autoComplete="current-password"
                    />
                    <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label="Remember me"
                    />
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                        onClick={handleSubmit}
                    >
                        Sign In
                    </Button>
                    <Grid container>
                        <Grid item>
                            <Link onClick={() => history.push('/register')} variant="body2">
                                {"Don't have an account? Sign Up"}
                            </Link>
                        </Grid>
                    </Grid>
                </form>
            </div>
        </Container>
    );
}

export default UserSignIn;
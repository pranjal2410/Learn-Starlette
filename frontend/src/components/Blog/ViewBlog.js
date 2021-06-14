import React from 'react';
import {
    makeStyles,
    Card,
    CardActions,
    CardMedia,
    CardContent,
    Grid,
    Typography,
    Button,
    Container,
    TextField
} from '@material-ui/core';
import {useHistory} from "react-router";
import Axios from "axios";

const useStyles = makeStyles((theme) => ({
    heroContent: {
        backgroundColor: theme.palette.background.paper,
        padding: theme.spacing(8, 0, 6),
    },
    heroButtons: {
        marginTop: theme.spacing(4),
    },
    cardGrid: {
        paddingTop: theme.spacing(8),
        paddingBottom: theme.spacing(8),
    },
    card: {
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
    },
    cardMedia: {
        paddingTop: '56.25%', // 16:9
    },
    cardContent: {
        flexGrow: 1,
    },
    footer: {
        backgroundColor: theme.palette.background.paper,
        padding: theme.spacing(6),
    },
}));

const ViewBlog = () => {
    const classes = useStyles();
    let history = useHistory();
    const [data, setData] = React.useState({
        blog: '',
        image: []
    });
    const [cards, setCards] = React.useState([1, 2, 3, 4, 5, 6])

    React.useEffect(() => {
        if(!sessionStorage.getItem('token'))
            history.push('/')
        // Axios.get(`${process.env.REACT_APP_API_URL}/blog`,
        //     {
        //         headers: {
        //             'Authorization': `Bearer ${sessionStorage.getItem('token')}`
        //         }
        //     })
        //     .then(res => {
        //         setCards(res.data);
        //     })
        // eslint-disable-next-line
    }, [])

    const handleChange = (event) => {
        if(event.target.id==='image') {
            var file = event.target.files[0];
            const reader = new FileReader();
            var url = reader.readAsDataURL(file);

            reader.onloadend = function(e) {
                setData({
                    ...data,
                    image: [reader.result]
                });
            }
            console.log(url);
            setData({
                ...data,
                [event.target.id]: event.target.files[0]
            })
        }
        else
            setData({
                ...data,
                [event.target.id]: event.target.value
            })
    }

    const handleSubmit = async() => {
        console.log(data);
    }

    return (
        <React.Fragment>
            <main>
                {/* Hero unit */}
                <div className={classes.heroContent}>
                    <Container maxWidth="sm">
                        <Typography component="h1" variant="h2" align="center" color="textPrimary" gutterBottom>
                            Create Blog
                        </Typography>
                        <Typography variant="h5" align="center" color="textSecondary" paragraph>
                            Something short and leading about the collection below—its contents, the creator, etc.
                            Make it short and sweet, but not too short so folks don&apos;t simply skip over it
                            entirely.
                        </Typography>
                        <TextField
                            id='blog'
                            name='blog'
                            rows={5}
                            variant='outlined'
                            multiline
                            label='Create Blog'
                            onChange={handleChange}
                            placeholder='Write Something....'
                            fullWidth
                        />
                        <div className={classes.heroButtons}>
                            <Grid container spacing={2} justify="center">
                                <Grid item>
                                    <input
                                        accept="image/*"
                                        type="file"
                                        id="image"
                                        name="image"
                                        onChange={handleChange}
                                        style={{ display: "none" }}
                                    />
                                    <label htmlFor="image">
                                        <Button variant="outlined" color="primary" component="span">
                                            Upload Image
                                        </Button>
                                    </label>
                                </Grid>
                                <Grid item>
                                    <Button variant="outlined" color="primary" onClick={handleSubmit}>
                                        Post Blog
                                    </Button>
                                </Grid>
                            </Grid>
                        </div>
                    </Container>
                </div>
                <Container className={classes.cardGrid} maxWidth="md">
                    {/* End hero unit */}
                    <Grid container spacing={4}>
                        {cards.map((card) => (
                            <Grid item key={card} xs={12} sm={6} md={4}>
                                <Card className={classes.card}>
                                    <CardMedia
                                        className={classes.cardMedia}
                                        image="https://source.unsplash.com/random"
                                        title="Image title"
                                    />
                                    <CardContent className={classes.cardContent}>
                                        <Typography gutterBottom variant="h5" component="h2">
                                            Heading
                                        </Typography>
                                        <Typography>
                                            This is a media card. You can use this section to describe the content.
                                        </Typography>
                                    </CardContent>
                                    <CardActions>
                                        <Button size="small" color="primary">
                                            View
                                        </Button>
                                        <Button size="small" color="primary">
                                            Edit
                                        </Button>
                                    </CardActions>
                                </Card>
                            </Grid>
                        ))}
                    </Grid>
                </Container>
            </main>
        </React.Fragment>
    );
}

export default ViewBlog;
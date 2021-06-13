import * as React from "react";
import {
    Typography,
    Paper,
    Grid
} from "@material-ui/core";
import {motion} from "framer-motion";

const UserRegistration = (props) => {
    return (
        <Grid container direction="row" spacing={2} justify="center">
            <Grid item xs={12}>
                <Typography
                    variant='h3'
                    component={motion.h3}
                    initial={{ opacity: 0, scale: 0 }}
                    animate={{ opacity: 1, scale: 1}}
                >
                </Typography>
            </Grid>
        </Grid>
    )
}
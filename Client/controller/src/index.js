const express = require("express");
const cors = require("cors");
const axios = require("axios");

const rootRoute = require("../routes/root.route");

//define server
const app = express();
const port = 8080 || process.env.PORT;

//middlewares
app.use(express.json());
app.use(cors());

//routes
app.use("/", rootRoute);

app.listen(port, () => {
  console.log(`Server is running on port 4000`);
});

const express = require("express");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

const port = 4000 || process.env.PORT;



app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

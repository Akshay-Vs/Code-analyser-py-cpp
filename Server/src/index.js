const express = require("express");
const cors = require("cors");

const problemRouter = require("./routes/problem");
const resultRouter = require("./routes/result");

const app = express();
app.use(express.json());
app.use(cors());

const port = 5000 || process.env.PORT;

app.use("/problem", problemRouter);
app.use("/submit", resultRouter);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

const express = require("express");
const cors = require("cors");
const fs = require('fs');
const path = require('path');

const app = express();
app.use(express.json());
app.use(cors());

const port = 5000 || process.env.PORT;

app.post("/submit", (req, res) => {
  console.log(req.body);
  const { userId, problemId, time, status } = req.body;

  res.send("Success");
});


app.get("/problem/:id", (req, res) => {
  const filePath = path.join(__dirname, '../static/rounds', `round_${req.params.id}.zip`);

  fs.access(filePath, fs.constants.F_OK, (err) => {
    if (err) {
      console.log(`File doesn't exist: ${err}`);
      res.status(404).send('File not found');
    } else {
      res.setHeader('Content-Type', 'application/zip');
      const fileStream = fs.createReadStream(filePath);
      fileStream.pipe(res);
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

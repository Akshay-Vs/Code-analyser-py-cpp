const router = require("express").Router();
const fs = require("fs");
const path = require("path");

router.get("/:id", (req, res) => {
  const filePath = path.join(
    __dirname,
    "../../static/rounds",
    `round_${req.params.id}.zip`
  );

  fs.access(filePath, fs.constants.F_OK, (err) => {
    if (err) {
      console.log(`File doesn't exist: ${err}`);
      res.status(404).send("File not found");
    } else {
      console.log(`File exists: ${filePath}`);
      res.setHeader("Content-Type", "application/zip");
      const fileStream = fs.createReadStream(filePath);
      fileStream.pipe(res);
    }
  });
});

module.exports = router;

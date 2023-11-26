const router = require("express").Router();
// const db = require("../lib/database");

router.post("/", (req, res) => {
  console.log(req.body);
  const { username, problemId, time, status } = req.body;
  // try {
  //   const result = db.insertData(username, problemId, time);
  //   res.send({ message: "Success" });
  // } catch (err) {
  //   console.log(err);
  //   res.send({ message: "Bad Gateway, DB failure" });
  // }
  console.log("Data is not inserted to DB, but the request is received")
  res.send({ message: "Success" });
});

module.exports = router;

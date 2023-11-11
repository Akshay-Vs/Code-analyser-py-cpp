const router = require("express").Router();

const endpoints = {
  "/": { endpoints: "GET all endpoints", type: "GET" },
  "/rounds/:id": { endpoints: "GET round by id", type: "GET" },
  "rounds/:id/time":
};

router.get("/", (req, res) => {
  res.send(
    `<ul>${Object.keys(endpoints)
      .map(
        (endpoint) =>
          `<li><a href="${endpoint}">${endpoint}</a>: <b>${endpoints[endpoint]}</b></li>`
      )
      .join("")}</ul>`
  );
});

module.exports = router;

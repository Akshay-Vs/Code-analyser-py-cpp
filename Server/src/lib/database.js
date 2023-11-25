const mysql = require("mysql2");
require("dotenv").config();

const pool = mysql
  .createPool({
    host: "127.0.0.1",
    user: "root",
    database: "bugbusters",
    password: "Fedora@74670",
  })
  .promise();

const endPool = async () => await pool.end();

const insertData = async (username, problemId, time) => {
  // Check if username exists
  const [rows] = await pool.query("SELECT * FROM score WHERE username = ?", [
    username,
  ]);

  if (rows.length > 0) {
    // If username exists, update the problemId column
    console.log(`\x1b[32mUser Exists, Updating problem_${problemId}...\x1b[0m`);

    const updateQuery = `UPDATE score SET problem_${problemId} = ? WHERE username = ? AND problem_${problemId} IS NULL`;
    return await pool.query(updateQuery, [time, username]);
  } else {
    // If username doesn't exist, insert a new row
    console.log(
      `\x1b[31mUser Doesn't Exist, Creating User, inserting_${problemId}...\x1b[0m`
    );
    const insertQuery = `INSERT INTO score (username, problem_${problemId}) VALUES (?, ?)`;
    return await pool.query(insertQuery, [username, time]);
  }
};

module.exports = { insertData, endPool };

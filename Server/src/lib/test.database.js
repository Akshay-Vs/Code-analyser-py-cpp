const { insertData, endPool } = require("./database");

const generateRandomHex = (length) => {
  let result = "";
  for (let i = 0; i < length; i++) {
    result += Math.floor(Math.random() * 16).toString(16);
  }
  return result;
};
(async () => {
  for (let i = 0; i < 75; i++) {
    const username = `user_${generateRandomHex(14)}`;
    console.log(`\x1b[36mInserting data for${username}}...\x1b[0m`);

    for (let j = 0; j < 4; j++) {
      const time = Math.random() * 100; // Generate a random time
      console.log(
        `\x1b[32m\tInserting data for problem ${j} with time ${time}\x1b[0m`
      );

      await insertData(username, j, time);
    }
  }
  await endPool();
})().catch(console.error);

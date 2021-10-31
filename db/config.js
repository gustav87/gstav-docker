db.createUser({
  user: "gstav",
  pwd: "ost",
  roles: [
    {
      role: "readWrite",
      db: "mydb",
    },
  ],
});

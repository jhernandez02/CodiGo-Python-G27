const bcrypt = require('bcryptjs');

const salt = bcrypt.genSaltSync(10);
const hash = bcrypt.hashSync("123456", salt);
console.log('salt:',salt);
console.log('hash:',hash);
bcrypt.compare("123456", hash, (err, res) => {
    console.log(res)
});
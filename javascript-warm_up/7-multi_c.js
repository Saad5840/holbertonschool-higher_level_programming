const arg = process.argv[2];
const count = parseInt(arg, 10);

if (isNaN(count) || count <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const uniqueNums = [...new Set(args)];
  uniqueNums.sort((a, b) => b - a);
  console.log(uniqueNums.length > 1 ? uniqueNums[1] : 0);
}

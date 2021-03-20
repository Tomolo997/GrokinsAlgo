let list = [1, 2, 3, 4, 5, 6, 7];

const bintarySearch = (list, item) => {
  let low = 0;
  let high = list.length - 1;
  while (low <= high) {
    let mid = (low + high) / 2;
    let guess = list[mid];
    if (guess === item) {
      return mid;
    } else if (guess > item) {
      high = mid - 1;
    } else if (guess < item) {
      low = mid + 1;
    } else {
      return null;
    }
  }
};

console.log(bintarySearch(list, 98));

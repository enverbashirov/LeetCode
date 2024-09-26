/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    // let c = 0
    // args.forEach((x, i) => c++);
    // return c

    return args.length
};

console.log(argumentsLength(1, 2, 3)); // 3
/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */
class Polygon {
    constructor(sides) {
        this.sides = sides;
    }

    //Perimeter method
    perimeter() {
        let total = 0;
        this.sides.forEach(
            function (side) {
                total += side;
            }
        );
        return total;
    }
}

// ===============================
    // Code in stub below //
// ===============================

const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
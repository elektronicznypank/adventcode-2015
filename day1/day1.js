"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var floor_index = fs.readFileSync('input.txt', 'utf-8');
function count_by_character(input_character) {
    var counter = 0;
    if (input_character == '(') {
        counter++;
    }
    else if (input_character == ')') {
        counter--;
    }
    return counter;
}
function count_santa_floor_and_basement(floors_input, target_index) {
    if (target_index === void 0) { target_index = -1; }
    var brackets_counter = 0;
    var basement_index = null;
    for (var floor_index_1 = 0; floor_index_1 < floors_input.length; floor_index_1++) {
        brackets_counter = brackets_counter + count_by_character(floors_input[floor_index_1]);
        if (brackets_counter == target_index && basement_index == null) {
            basement_index = floor_index_1 + 1;
        }
    }
    return [brackets_counter, basement_index];
}
var final_floor = count_santa_floor_and_basement(floor_index)[0];
var basement_floor_index = count_santa_floor_and_basement(floor_index)[1];
console.log("The instructions take Santa to floor ".concat(final_floor, " and the position of the first character taking Santa to the target floor is ").concat(basement_floor_index, "."));

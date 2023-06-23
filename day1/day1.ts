import * as fs from 'fs';
const floor_index: string = fs.readFileSync('input.txt', 'utf-8');

function count_by_character(input_character: string) {
    
    let counter: number = 0
    if (input_character == '(') {
        counter++;
    }
    else if (input_character == ')') {
        counter--;
    }
    return counter;
}


function count_santa_floor_and_basement(floors_input: string, target_index: number = -1) {
    
    let brackets_counter: number = 0;
    let basement_index: number | null = null;

    for (let floor_index: number = 0; floor_index < floors_input.length; floor_index++) {
        
        brackets_counter = brackets_counter + count_by_character(floors_input[floor_index]);
        
        if (brackets_counter == target_index && basement_index == null) {
            basement_index = floor_index + 1;
        } 

    }
    
    return [brackets_counter, basement_index];
}

let final_floor = count_santa_floor_and_basement(floor_index)[0];
let basement_floor_index = count_santa_floor_and_basement(floor_index)[1];

console.log(`The instructions take Santa to floor ${final_floor} and the position of the first character taking Santa to the target floor is ${basement_floor_index}.`);